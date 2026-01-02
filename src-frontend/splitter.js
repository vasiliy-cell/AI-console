// src-frontend/splitter.js

const app = document.getElementById("app");
const splitter = document.getElementById("splitter");
const leftPanel = document.getElementById("terminal-panel");
const rightPanel = document.getElementById("ai-panel");

let isDragging = false;

splitter.addEventListener("mousedown", () => {
  isDragging = true;
  document.body.style.cursor = "col-resize";
  document.body.style.userSelect = "none";
});

document.addEventListener("mouseup", () => {
  if (!isDragging) return;

  isDragging = false;
  document.body.style.cursor = "";
  document.body.style.userSelect = "";

  // ⬅ финальный принудительный resize терминала
  document.dispatchEvent(new Event("terminal-resize"));
});

document.addEventListener("mousemove", (e) => {
  if (!isDragging) return;

  const styles = getComputedStyle(app);
  const paddingLeft = parseFloat(styles.paddingLeft);
  const paddingRight = parseFloat(styles.paddingRight);

  const rect = app.getBoundingClientRect();
  const splitterWidth = splitter.getBoundingClientRect().width;
  const minWidth = 200;

  const leftWidth = e.clientX - rect.left - paddingLeft;
  const availableWidth =
    rect.width - paddingLeft - paddingRight - splitterWidth;

  const rightWidth = availableWidth - leftWidth;

  if (leftWidth < minWidth || rightWidth < minWidth) return;

  leftPanel.style.flex = "none";
  rightPanel.style.flex = "none";

  leftPanel.style.width = `${leftWidth}px`;
  rightPanel.style.width = `${rightWidth}px`;

  // ⬅ КЛЮЧЕВО: сообщаем терминалу о resize
  document.dispatchEvent(new Event("terminal-resize"));
});
