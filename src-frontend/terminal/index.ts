import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";

export function initTerminal() {
  const term = new Terminal({
    cursorBlink: true,
    // Оставляем тему пустой, чтобы CSS мог перекрывать цвета
    theme: {}, 
  });

  const fitAddon = new FitAddon();
  term.loadAddon(fitAddon);

  const container = document.getElementById('terminal-panel');
  if (!container) {
    console.error("Контейнер #terminal-panel не найден!");
    return null;
  }

  term.open(container);

  // Небольшая задержка для корректного расчета размера
  setTimeout(() => fitAddon.fit(), 10);

  window.addEventListener('resize', () => fitAddon.fit());

  return { term, fitAddon };
}
