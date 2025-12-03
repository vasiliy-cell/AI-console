from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button
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
        border: round $accent;
        margin: 1 1;
        background: $surface-darken-3;
    }

    #right-panel {
        width: 1fr;
        border: round $accent;
        margin: 1 1 1 0;
        background: $surface-darken-3;
        layout: vertical; /* Используем vertical layout для размещения элементов друг под другом */
        padding: 1; /* Добавим немного отступа внутри панели */
    }

    /* Новый класс для "распорки", которая занимает все доступное пространство */
    .spacer {
        height: 1fr; 
        /* Мы можем оставить его пустым, он просто будет растягиваться */
    }

    /* Контролы больше не нуждаются в auto-margin */
    #right-panel-controls {
        height: auto; 
    }

    Input {
        width: 1fr;
        margin-bottom: 1; 
        border: round $accent;
        background: $surface-darken-3;
    }

    #button-container {
        layout: horizontal;
        height: auto;
    }

    Button {
        width: 1fr; 
        margin-right: 1;
        border: round $accent;
        background: $surface-darken-3;
    }
    
    Button:last-child {
        margin-right: 0;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal(id="main-area"):
            with Container(id="left-panel"):
                yield Static(id="term")
            
            with Container(id="right-panel"):
  
                yield Static(classes="spacer") 
                
                with Vertical(id="right-panel-controls"):
                    yield Input(placeholder="", id="user-input")
                    with Horizontal(id="button-container"):
                        yield Button("Answer", id="btn-answer")
                        yield Button("Run", id="btn-run")



if __name__ == "__main__":
    AICLI().run()
