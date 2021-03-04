#!/usr/bin/env bash

if [[ $(tmux ls)  == *"barterDev"* ]]; then
  tmux kill-session -t barterDev
fi
tmux new-session -d -s barterDev -n components 
tmux send-keys -t barterDev 'cd backend; clear; python manage.py runserver' 'C-m'
tmux split-window -t barterDev 
tmux send-keys -t barterDev 'cd web; clear; npm run serve' 'C-m'

tmux attach-session -t barterDev
