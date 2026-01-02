import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";


import { registerFitAddon, fitTerminal } from "../resize";

export function initTerminal() {
  const term = new Terminal({
    cursorBlink: true,
    theme: {}, 
  });

  const fitAddon = new FitAddon();
  term.loadAddon(fitAddon);

  // ⬅ регистрируем addon глобально
  registerFitAddon(fitAddon);

  const container = document.getElementById("terminal-panel");
  if (!container) {
    console.error("Контейнер #terminal-panel не найден!");
    return null;
  }

  term.open(container);

  // ⬅ важно для Tauri Linux
  setTimeout(() => fitTerminal(), 50);

  // resize окна
  window.addEventListener("resize", fitTerminal);

  // resize от splitter
  document.addEventListener("terminal-resize", fitTerminal);

  return { term, fitAddon };
}
