from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive # Для реактивной переменной

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
        overflow-y: scroll;          /* Важно! Чтобы старые сообщения были видны */
    }

    #right-panel {
        width: 1fr;
        border: round $accent;
        margin: 1 1 1 0;
        background: $surface-darken-3;
        layout: vertical; /* Используем vertical layout для размещения элементов друг под другом */
        padding: 1; /* Добавим немного отступа внутри панели */
        overflow-y: scroll;          /* Важно! Чтобы старые сообщения были видны */
    }

    /* Новый класс для "распорки", которая занимает все доступное пространство */
    .spacer {
        height: 0.4fr; 
        width: 0.4fr; 
    }

    /* Контролы больше не нуждаются в auto-margin */
    #right-panel-controls {
        height: auto; 
    }

    Input {
        width: 1fr;
        margin-bottom: 0; 
        border: round $accent;
        background: $surface-darken-3;
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







if __name__ == "__main__":
    AICLI().run()
