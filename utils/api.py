import requests
from config_loader import load_api_key, ConfigError
from errors import APIError

DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

def send_request(prompt: str) -> str:
    """Send prompt to DeepSeek and return assistant's reply."""
    try:
        api_key = load_api_key()

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(DEEPSEEK_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    except requests.RequestException as e:
        raise APIError(f"Request failed: {e}") from e
    except KeyError as e:
        raise APIError("Invalid API response format") from e
    except ConfigError as e:
        raise APIError(f"Config error: {e}") from e


if __name__ == "__main__":
    test_prompt = "Привет, кто ты?"
    try:
        print("Sending:", test_prompt)
        reply = send_request(test_prompt)
        print("Assistant:", reply)
    except APIError as e:
        print("APIError:", e)

