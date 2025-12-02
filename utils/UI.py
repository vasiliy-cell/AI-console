from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button, Footer, Header
from textual.containers import Container, Horizontal, Vertical


class AICLI(App):
    CSS = """
    Screen {
        layout: vertical;
        background: $surface-darken-3;  
    }

    #main-area {
        height: 1fr;
        layout: horizontal;
    }

    #left-panel {
        width: 2fr;          
        border: tall $accent;
        margin: 1 1;
        background: $surface-darken-3;
        border: round $primary;  
    }

    #right-panel {
        width: 1fr;         
        border: tall $accent;
        margin: 1 1 1 0;
        background: $surface-darken-3;
        border: round $primary;  
        

    }

    #bottom-bar {
        height: 3;
        dock: bottom;
        margin-bottom: 2;
    }

    Input {
        width: 1fr;
        margin-right: 1;
        border: round ;  
        background: $surface-darken-3;
    }

    Button {
        margin-right: 1;
        border: round ; 
        background: $surface-darken-3; 
    }

#   Button#btn-answer {
#     background: $accent;
#     color: $text;
#     }

    Footer { height: 1; }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        # Основная область — горизонтально делим 2:1
        with Horizontal(id="main-area"):
            with Container(id="left-panel"):
                yield Static(id="term")

            with Container(id="right-panel"):
                yield Static()

        # Нижняя панель ввода
        with Horizontal(id="bottom-bar"):
            yield Input(placeholder="")
            yield Button("Answer", id="btn-answer")
            yield Button("Run", id="btn-run")
            yield Button("CLI", id="btn-cli")

        yield Footer()


if __name__ == "__main__":
    AICLI().run()



