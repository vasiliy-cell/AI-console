import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import "@xterm/xterm/css/xterm.css";

export function initTerminal() {
  const term = new Terminal({
    cursorBlink: true,
    theme: {
      background: '#161617', // Под цвет вашего конфига
    },
    allowProposedApi: true
  });

  const fitAddon = new FitAddon();
  term.loadAddon(fitAddon);

  const container = document.getElementById('terminal-panel')!;
  term.open(container);

  // Важно: fit() работает только если контейнер имеет физический размер
  fitAddon.fit();

  // Подстраиваем размер при изменении окна
  window.addEventListener('resize', () => fitAddon.fit());

  return { term, fitAddon };
}
