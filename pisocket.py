import socket

HOST = 'IP of local (client) machine'
PORT = 6001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'

s.bind((HOST, PORT))

s.listen(1)

print 'Socket awaiting data'

conn, addr = s.accept()

print 'Connected to: ' + str(addr)

while True:
   data = conn.recv(1024)
   if not data:
      break
   print "data from esp8266: " + str(data)
c.close()
