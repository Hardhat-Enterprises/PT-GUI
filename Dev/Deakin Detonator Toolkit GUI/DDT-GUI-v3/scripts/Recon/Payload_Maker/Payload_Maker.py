import PySimpleGUI as sg
import os

#Creating program function
def MAKE_Payload_Maker():
	main_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(main_path)
	#layout = [ [] ]
	#Obtains the current working directory
	os.popen("chmod 755 exploit.sh")
	os.popen("xterm ./exploit.sh")
	#return sg.Window('Payload_Maker', layout, size=(0,0), finalize=True)
    
def CHECK_Payload_Maker(window, event, values):
	os.chdir('../..')
	#window.close()
		