from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button, Footer, Header
from textual.containers import Container, Horizontal, Vertical


class AICLI(App):
    CSS = """
    Screen {
        layout: vertical;
    }

    #main-area {
        height: 1fr;
        layout: horizontal;
    }

    #left-panel {
        width: 2fr;          
        border: tall $primary;
        margin: 1 1;
        background: $surface-darken-3;
    }

    #right-panel {
        width: 1fr;         
        border: tall $secondary;
        margin: 1 1 1 0;
        background: $surface-darken-3;
    }

    #bottom-bar {
        height: 3;
        dock: bottom;
        margin-bottom: 2;
    }

    Input {
        width: 1fr;
        margin-right: 1;
    }

    Button {
        margin-right: 1;
    }

    Footer { height: 1; }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        # Основная область — горизонтально делим 2:1
        with Horizontal(id="main-area"):
            with Container(id="left-panel"):
                yield Static("Левая панель (терминал/чат)\n2/3 ширины", id="term")

            with Container(id="right-panel"):
                yield Static("Правая панель\n1/3 ширины\n(инфо, история, настройки и т.д.)")

        # Нижняя панель ввода
        with Horizontal(id="bottom-bar"):
            yield Input(placeholder="Введите сообщение...")
            yield Button("Answer", id="btn-answer")
            yield Button("Run", id="btn-run")
            yield Button("CLI", id="btn-cli")

        yield Footer()


if __name__ == "__main__":
    AICLI().run()



