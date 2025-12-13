from textual.app import App, ComposeResult
from textual.widgets import Input, Markdown, Static
from textual.containers import Horizontal, Vertical, Container
from api import stream_request, APIError


class AICLI(App):
    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Container():
                yield Markdown("", id="api-output")
                yield Static(classes="spacer")
                with Vertical():
                    yield Input(id="user-input")

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        prompt = event.value.strip()
        event.input.value = ""

        if not prompt:
            return

        output = self.query_one("#api-output", Markdown)
        output.update("**Assistant:**\n\n")

        full_text = ""

        try:
            async for token in stream_request(prompt):
                full_text += token
                output.update(f"**Assistant:**\n\n{full_text}")

        except APIError as e:
            output.update(f"**API Error:** `{e}`")


if __name__ == "__main__":
    AICLI().run()
