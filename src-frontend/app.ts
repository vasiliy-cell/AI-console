import { initTerminal } from "./terminal/index"; // проверьте путь к файлу
// Подключаем ВАШ файл стилей. Теперь он главный.
import "./terminal/terminal.css"; 

window.onload = () => {
  const result = initTerminal();
  
  if (result) {
    const { term } = result;
    term.write('AICLI Terminal \x1b[32mInitialized\x1b[0m\r\n$ ');
  }
};
