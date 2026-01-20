import asyncio
import json
import sys
from api import stream_request



# создание задачи под каждый AI-запрос
tasks: dict[str, asyncio.Task] = {}



# handle_prompt это 1 запрос польователя 
async def handle_prompt(req_id: str, text: str):
    try:

        # stream_request это асинхронный генератор
        # .dumps делайт из пайтон элемета JSON-formatted string
# flush=True сразу чистит и не дает копить текст в  буфере 
        async for token in stream_request(text):
# Отправка токенов
            print(json.dumps({
                "type": "token",
                "id": req_id,
                "text": token
            }), flush=True)
        print(json.dumps({
            "type": "done",
            "id": req_id
        }), flush=True)
# {"type": "done"}  это Завершение
# Rust/Frontend должны знать, что:
# поток закончился
# можно разблокировать UI
# можно убрать spinner


    except asyncio.CancelledError:
        # это Abort


#         Когда ты вызываешь:
# task.cancel()
# Python:
# кидает CancelledError внутрь корутины
# на ближайшем await
# Ты его:
# ловишь
# отправляешь "aborted"
# пробрасываешь дальше (raise)
# Почему raise важен:
# иначе задача будет считаться «успешно завершённой»
        print(json.dumps({
            "type": "aborted",
            "id": req_id
        }), flush=True)
        raise

    except Exception as e:
        print(json.dumps({
            "type": "error",
            "id": req_id,
            "message": str(e)
        }), flush=True)


async def stdin_loop():


# Это главный цикл сервиса.
# Он:
# живёт вечно
# читает stdin
# реагирует на команды


    loop = asyncio.get_running_loop()

    while True:
        line = await loop.run_in_executor(None, sys.stdin.readline)

        if not line:
            await asyncio.sleep(0.05)
            continue

        try:
            msg = json.loads(line.strip())
        except json.JSONDecodeError:
            continue

        msg_type = msg.get("type")
        req_id = msg.get("id")

        if msg_type == "prompt":
            text = msg.get("text", "")

            # если такой id уже есть — сначала убьём
            if req_id in tasks:
                tasks[req_id].cancel()

            task = asyncio.create_task(handle_prompt(req_id, text))
            tasks[req_id] = task

        elif msg_type == "abort":
            task = tasks.get(req_id)
            if task:
                task.cancel()
                del tasks[req_id]


async def main():
    await stdin_loop()


if __name__ == "__main__":
    asyncio.run(main())
