#/bin/bash
username=$(zenity --entry --text "Please Enter Desired Username to lookup" --title "DDT");
# This prompts the user for the username they would like to investigate

finished=0
cewl=0
#setting up future variables

tmux new -d -s Gen
tmux send-keys -t Gen.0 "./sherlock.py $username"
tmux send-keys -t Gen.0 Enter
# Sending the users input to sherlock to create a website list

while true
do
  FILE=$username.txt
  if test -f "$FILE" ; then
    echo "Website List Created"
    finished=1
    # Variable set to 1 to trigger next event
    break
  else
    echo "Doxxing Username..."
    sleep 2
  fi
done
# Loop to check if sherlock has finished

if [ $finished -eq 1 ]
# Event triggered by sherlock file being created
then
  oldIFS="$IFS"
  IFS=$'\n' arr=($(<$username.txt))
  IFS="$oldIFS"
  # https://stackoverflow.com/questions/30988586/creating-an-array-from-a-text-file-in-bash?lq=1
  # jahid
  # This stores the output of sherlock into an array which we can access later
  lines=$(grep "" -c $username.txt)
  # https://askubuntu.com/questions/442914/calculating-the-number-of-lines-in-a-file
  # andreykyz
  lines=$((lines-2))
  # Removes the line count by 2 as arrays count from 0 and the last line does not contain a URL
  # DEBUG LINE echo "this is the number of lines: $lines"
  # http://shell-tips.com/bash/math-arithmetic-calculation/
  cewl=1
  # To Trigger next event
fi

count=0
while [[ $cewl -eq 1 ]] && [[ $count -le $lines ]]
# When the event is triggered and count is less than or equal to the amount of lines in the file. This is to cycle through every entry in the array
do
  echo $count
  tmux new -d -s Cewl$count
  tmux send-keys -t Cewl$count.0 "cewl -w $username$count -d 1 -m 5 ${arr[$count]}"
  # Sending the first entry to Cewl. The count variable is also used to name the wordlists ($username$count)
  tmux send-keys -t Cewl$count.0 Enter
  count=$((count+1))
  # This is to access the next entry in the array. Note that line 50 does not allow the loop to exceed the maximum amount of entries in the array
  # DEBUG LINE echo $count
  # DEBUG LINE echo $cewl
done

exists=0
while true
do
  FILE=$username$exists
  if test -f "$FILE" ; then
    # Tests to see if $username$count file exists starting from 0th array to Nth array. $exists variable is used to have it independent to $count
    echo "Wordlist $exists created"
    exists=$((exists+1))
    # Cycle through array
    # DEBUG LINE echo "Finished = $exists/$lines"
  elif [ $exists -ge $lines ]; then
  ready=1
  #  DEBUG LINE echo $exists "/" $lines "Individual wordlists in total have been created"
  break
  fi
done

echo "Combining Wordlists"

touch wordlist_$username.txt
# Create the master wordlist file
combine=0
while [[ $combine -le $lines ]]
# This sets the maximum amount of wordlists files the program is looking for to append to the master file
do
  cat $username$combine >> wordlist_$username.txt
  sleep 5
  # Append to the master file and sleep for 5 to avoid errors
  combine=$((combine+1))
  # Cycle through all files
done


Wordlist=$(zenity --info --text "

Master wordlist created at wordlist_$username.txt"  --width 300 --height 127);
# Inform the user that the master wordlist has been created with the name of the file.

echo $Wordlist
