import socket


TCP_IP = u'192.168.1.121'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
file_desc = open('testing.txt', 'rb')

line = file_desc.read(BUFFER_SIZE)

while (line):
	print "sending..."
	s.send(line)
	line = file_desc.read(BUFFER_SIZE)

file_desc.close()

print 'DONE'
s.shutdown(socket.SHUT_WR)
print s.recv(BUFFER_SIZE)
s.close()
