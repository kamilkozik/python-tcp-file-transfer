import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

print "Creating socket..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Binding to broadcast:5005 ..."
s.bind((TCP_IP, TCP_PORT))
print "Creating buffer for 5 connections..."
s.listen(5)

while True:
	print "Waiting for connection..."
	conn, addr = s.accept()
	print "Getting file..."
	# print ""
	file_desc = open('received_file.txt', 'wb')	
	line = conn.recv(BUFFER_SIZE)
	# print "."
	while line:
		print '.'
		file_desc.write(line)
		line = conn.recv(BUFFER_SIZE)
		if not line:
			break
	file_desc.close()
	print "RECIEVING: DONE"
	conn.send('SERVER: DONE')
	conn.close()