from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Markdown
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive  # For the reactive variable
from api import send_request, APIError


class AICLI(App):
    CSS_PATH = "style.css"

    user_request = reactive("")

    def compose(self) -> ComposeResult:

        with Horizontal(id="main-area"):

            with Container(id="right-panel"):

                # Markdown вместо Static
                yield Markdown("", id="api-output")

                yield Static(classes="spacer")

                with Vertical(id="right-panel-controls"):
                    yield Input(placeholder="", id="user-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:

        if event.input.id == "user-input":
            user_text = event.value.strip()

            self.query_one("#user-input").value = ""

            if user_text:
                self.user_request = user_text
                print(f"New request: '{self.user_request}'")

                output_widget = self.query_one("#api-output", Markdown)
                output_widget.update("**Status:** Sending request...")

                try:
                    reply = send_request(prompt=self.user_request)

                    # Markdown поддерживается автоматически
                    output_widget.update(f"**Assistant:**\n\n{reply}")

                except APIError as e:
                    output_widget.update(f"**API Error:** `{e}`")


if __name__ == "__main__":
    AICLI().run()
