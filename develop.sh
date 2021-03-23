#!/usr/bin/env bash

if [[ $(tmux ls)  == *"barterDev"* ]]; then
  tmux kill-session -t barterDev
fi
tmux new-session -d -s barterDev -n components 
tmux send-keys -t barterDev './run_frontend.sh' 'C-m'
tmux split-window -t barterDev 
tmux send-keys -t barterDev './run_backend.sh' 'C-m'
tmux split-window -h -t barterDev 
tmux send-keys -t barterDev './run_db.sh' 'C-m'

tmux attach-session -t barterDev
