import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import "@xterm/xterm/css/xterm.css";

// Ждем полной загрузки DOM
window.onload = () => {
  const terminalContainer = document.getElementById('terminal-panel');

  if (!terminalContainer) {
    console.error("Контейнер #terminal-panel не найден!");
    return;
  }

  const term = new Terminal({
    cursorBlink: true,
    theme: {
      background: '#161617',
      foreground: '#ffffff',
    },
    fontSize: 14,
    fontFamily: 'Courier New'
  });

  const fitAddon = new FitAddon();
  term.loadAddon(fitAddon);

  // Открываем терминал в контейнере
  term.open(terminalContainer);

  // Важно: вызываем fit() через небольшую паузу, 
  // чтобы браузер успел рассчитать размеры flexbox
  setTimeout(() => {
    fitAddon.fit();
    term.write('AICLI Terminal \x1b[32mInitialized\x1b[0m\r\n$ ');
  }, 10);

  // Следим за изменением размера окна
  window.addEventListener('resize', () => {
    fitAddon.fit();
  });
};
