from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive # For the reactive variable
from api import send_request, APIError 

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
        overflow-y: scroll;          /* Important! So older messages are visible */
    }

    #right-panel {
        width: 1fr;
        border: round $accent;
        margin: 1 1 1 0;
        background: $surface-darken-3;
        layout: vertical; /* Use vertical layout to place elements below each other */
        padding: 1; /* Add some padding inside the panel */
        overflow-y: scroll;          /* Important! So older messages are visible */
    }
    
    /* Добавляем немного стиля для нового виджета вывода в правой панели */
    #api-output {
        height: auto; /* Позволяет тексту занимать нужное место */
        margin-bottom: 1;
        padding: 0 1;

    }


    /* New class for the "spacer" that takes up all available space */
    .spacer {
        height: 0.4fr; 
        width: 0.4fr; 
    }

    /* Controls no longer need auto-margin */
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

    user_request = reactive("")

    def compose(self) -> ComposeResult:

        with Horizontal(id="main-area"):
            with Container(id="left-panel"):    
                yield Static(id="term")
            
            with Container(id="right-panel"):
    
                yield Static("", id="api-output") 
                
                yield Static(classes="spacer") 
                
                with Vertical(id="right-panel-controls"):
                    yield Input(placeholder="", id="user-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        
        if event.input.id == "user-input":
            user_text = event.value.strip()
            
            self.query_one("#user-input").value = ""
            
            if user_text:  # Если строка не пустая, продолжаем обработку
                self.user_request = user_text
                print(f"New request: '{self.user_request}'")

                # Получаем ссылку на виджет вывода в правой панели
                output_widget = self.query_one("#api-output", Static)
                output_widget.update("Status: Sending request...")

                try:
                    # Отправляем запрос
                    reply = send_request(prompt=self.user_request)
                    output_widget.update(f"Assistant: {reply}")
                    
                except APIError as e:
                    output_widget.update(f"API Error: {e}")
                        

if __name__ == "__main__":
    AICLI().run()
