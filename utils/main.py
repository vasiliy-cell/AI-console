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


    async def on_input_submitted(self, event: Input.Submitted) -> None:
        user_request = event.value.strip()
        event.input.value = ""


        if not user_request:
            return

        output = self.query_one("#api-output", Markdown)
        output.update("**Assistant:**\n\n")

        full_text = ""

        try:
            async for token in stream_request(user_request):
                full_text += token
                output.update(f"**Assistant:**\n\n{full_text}")

        except APIError as e:
            output.update(f"**API Error:** `{e}`")


if __name__ == "__main__":
    AICLI().run()
