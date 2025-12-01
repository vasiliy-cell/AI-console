from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button, Footer, Header
from textual.containers import Horizontal, Vertical

class TerminalApp(App):
    CSS = """
    Screen {
        background: #0d1117;         
        color: #f0f6fc;
    }



    #left  { width: 2fr; background: $surface; }
    #right { width: 1fr; background: $panel; padding: 1; }
    Input { margin: 1 0; }
    .buttons { height: 3; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="left"):
                yield Static("Тут будет терминал (пока заглушка)", id="term")
            
            with Vertical(id="right"):
                yield Input(placeholder="Введи текст...")
                with Horizontal(classes="buttons"):
                    yield Button("Отправить", variant="primary")
                    yield Button("Очистить", variant="error")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.label == "Очистить":
            self.query_one("#term").update("")

app = TerminalApp()
if __name__ == "__main__":
    app.run()