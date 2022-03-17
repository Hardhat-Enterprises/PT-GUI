from subprocess import Popen, PIPE
import PySimpleGUI as sg
import subprocess
import os

main_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(main_path)

def runCommand(window, cmd):
    p1 = Popen(cmd, stdout=PIPE, universal_newlines=True)
    for line in p1.stdout:
        window['-OUTPUT-'+sg.WRITE_ONLY_KEY].print(line, end="")
        window.refresh()