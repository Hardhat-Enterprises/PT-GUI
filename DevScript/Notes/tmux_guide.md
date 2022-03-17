# TMUX (Terminal Multiplexer) Guide
Collected from tmux cheatsheet located [here](https://tmuxcheatsheet.com/).</br>
Full Manual Guide Located [here](https://man7.org/linux/man-pages/man1/tmux.1.html).</br>
Modern Manual Guide Located [here](http://manpages.ubuntu.com/manpages/bionic/man1/tmux.1.html#:~:text=command%20is%20assumed.-,KEY%20BINDINGS,in%20the%20current%20window%20forwards.)
---

## Introduction
TMUX is a terminal multiplexer used for Unix-like OS. It allows Multiple terminal sessions to run simultaneously in a single window.
Its useful for running more than one command-line program at the same time.
e.g. Using netcat to listen on a port runs the terminal for netcat only, therefore a new terminal must opened in order to run other cmds.

## Basics
#### Creating a new session with tmux
```tmux
tmux
tmux new
tmux new-session
```

#### Create a new session with a name
```tmux
tmux new -s Sesh1 #(<-- Name can be anything)
```

#### Create a new name for session and window
```tmux
tmux new -s mysession -n mywindow
```
#### Split a window horizontally or vertically
```tmux
tmux split-window -h or -v
```
#### Attach a session
```tmux
tmux a
tmux at             #Same as above
tmux attach         #Same as above
tmux attach-session #Same as above
```
To return to a session use "tmux a -t 0" </br>
Note: 0 is default if the session has no name. If you create another session, the next number will be used instead, which is 1, 2, 3 etc. Best to name the sessions.

#### Detach a session
```tmux
tmux detach #(Sends you back to your terminal)
```
#### Show tmux sessions
Search for sessions currently active
```tmux
tmux ls
```

#### Kill tmux terminal
```tmux
tmux kill-session
```
#### Kill every tmux session
```tmux
tmux kill-server
```
#### Exit session in tmux
This completely quits the session if you want to run the session and go back into your kali terminal use tmux detach
```tmux
exit
```
---

#### Send-keys command
Send a key or keys to a window
```tmux
tmux send-keys -t   # -t (target-pane)
```
Example
```tmux
# Create a new session with a name
tmux new -d -s test1
# send keystrokes in the Apostrophes.
tmux send-keys -t test1 'echo "Hello World"' C-m #C-m is the prefix for Enter in tmux.
# Reattaches the session to display result
tmux a -t test1
```

#### Splitting a tmux window and running scripts in each pane
Start a new tmux session and detach from it
```tmux
tmux new -d -s test1
```

Displays Pane 1
```tmux
tmux rename-window 'my window'
tmux send-keys 'echo "pane 1"' C-m
tmux send-keys -t test1 "cd /home/kali/scripts" C-m  #Cd into directory where scripts is placed
tmux send-keys -t test1 ./Script1.sh C-m  #Running Bash Scripts
```

Displays Pane 2 </br>
Note to switch panes in tmux press Ctrl+b then <- or ->

```tmux
tmux split-window -h
tmux send-keys 'echo "pane 2"' C-m
tmux send-keys -t test1 "cd /home/kali/scripts" C-m
tmux send-keys -t test1 "python3 Script2.py" C-m #Running Python Scripts
```

Displays Pane 3

```tmux
tmux split-window -h
tmux send-keys 'echo "pane 3"' C-m
tmux send-keys 'nc -l 192.168.1.1 -p 25'
```
Makes the panes layout evenly
```tmux
tmux select-layout even-horizontal
```
Attach session to display results
```tmux
tmux a -t test1
```

#### Default Key Bindings
The Prefix key for tmux is Ctrl-b. </br>
When running a tmux session first press the Ctrl+b keys then release and press the default key bindings of your choice.
Example </br>
Ctrl+b release -> (Switch to right pane)
or
Ctrl+b release c (create a new window)

Some Handy tmux Key Bindings
=========
| Key(s)  | Description |
| :-----: | ----------- |
| `CTRL`+`b` `<command>` | sends `<command>` to tmux instead of sending it to the shell |
| | **General Commands** |
| `?` | shows a list of all commands (`q`closes the list) |
| `:` | enter a tmux command |
| | **Windows** |
| `c` | creates a new window |
| `,` | rename current window |
| `$` | rename current session |
| `p` | switch to previous window |
| `n` | switch to next window |
| `w` | list windows (and then select with arrow keys) |
| `&` | kill current window |
| `0-9` | Select window 0 to 9 |
| | **Panes** |
| `%` | split window vertically |
| `"` | split window horizontally |
| `x` | kill current pane (prompts y/n)|
| ← → ↓ ↑ | change pane using directional keys |
| | **Sessions** |
| `d` | detach from session |

#### Customization
#### Toggling Status Line
Turn off
```tmux
tmux set-option status off
```
Turn on
```tmux
tmux set-option status on
```
---
