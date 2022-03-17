#/bin/bash
check=$(zenity --question --text "Do you want to host the enumeration tool?" --title "DDT";)
if [[ $? -eq 0 ]]
  then ipaddress=$(hostname -I) #grab the current IP address
  tmux new -d -s Web #create an external terminal to host the web server
  tmux send-keys -t Web.0 "python3 -m http.server 80"
  tmux send-keys -t Web.0 Enter
  #run web server and send "enter" key

  Response=$(zenity --info --text "

  Enumeration tool is hosted on:

  http:// $ipaddress

  Click OK to stop the Web Server"  --width 300 --height 127);
  # Create the info popup box with the URL to the server.
  echo $Response
fi
if [ $? -eq 0 ]
  then tmux kill-session
fi
