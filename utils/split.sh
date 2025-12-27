#!/bin/bash

SESSION_NAME="AICLI"

# Абсолютный путь к директории, где лежит ЭТОТ скрипт и main.py
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Создаём новую сессию tmux (левая панель — текущая директория)
tmux new-session -d -s "$SESSION_NAME"

# Делим окно на две панели
tmux split-window -h

# Равные размеры
tmux select-layout even-horizontal

# Переходим в правую панель
tmux select-pane -R

# В правой панели: переходим в папку скрипта и запускаем main.py
tmux send-keys "cd \"$SCRIPT_DIR\" && python3 main.py" C-m

# Подключаемся
tmux attach-session -t "$SESSION_NAME"
