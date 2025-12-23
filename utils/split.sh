SESSION_NAME="AICLI"

# Создаём новую сессию tmux
tmux new-session -d -s "$SESSION_NAME"

# Делим окно на две панели (вертикально)
tmux split-window -h

# (опционально) равные размеры панелей
tmux select-layout even-horizontal

# Подключаемся к сессии
tmux attach-session -t "$SESSION_NAME"