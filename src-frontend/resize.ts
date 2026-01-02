import { FitAddon } from "@xterm/addon-fit";

let fitAddon: FitAddon | null = null;

export function registerFitAddon(addon: FitAddon) {
  fitAddon = addon;
}

export function fitTerminal() {
  if (!fitAddon) return;

  // ВАЖНО: 2 кадра
  requestAnimationFrame(() => {
    fitAddon!.fit();
    requestAnimationFrame(() => {
      fitAddon!.fit();
    });
  });
}
