from textual.app import App, ComposeResult
from textual.widgets import Input, Markdown, Static
from textual.containers import Horizontal, Vertical, Container
from api import stream_request, APIError


class AICLI(App):
    CSS_PATH = "style.css"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ascii_art = self.load_ascii_art_file()

    def load_ascii_art_file(self):
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "ASCII.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "ASCII art file not found."

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Container():
                yield Markdown("", id="api-output")
                yield Static(classes="spacer")
                with Vertical():
                    yield Input(id="user-input")
                    yield Static(self.ascii_art, id="ascii-art")
                    yield Static("Hey there! Let’s jump in", id="welcome-text1") 
                    yield Static("linux is the best OS", id="welcome-text2") 


    async def on_input_submitted(self, event: Input.Submitted) -> None:
        user_request = event.value.strip()
        event.input.value = ""


        if not user_request:
            return

        output = self.query_one("#api-output", Markdown)
        output.update("**Assistant:**\n\n")



        # Получаем ссылку на элементы, которые нужно скрыть
        welcome_text1 = self.query_one("#welcome-text1", Static)
        welcome_text2 = self.query_one("#welcome-text2", Static)
        ascii_art = self.query_one("#ascii-art", Static)

        # Скрываем приветственные тексты и ASCII-арт
        welcome_text1.update("")
        welcome_text2.update("")
        ascii_art.update("")





        full_text = ""

        try:
            async for token in stream_request(user_request):
                full_text += token
                output.update(f"**Assistant:**\n\n{full_text}")

        except APIError as e:
            output.update(f"**API Error:** `{e}`")


if __name__ == "__main__":
    AICLI().run()
