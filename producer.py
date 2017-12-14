import hashlib 
from time import sleep
from socket import socket

sock = socket()
sock.connect(('192.168.0.35', 54321))


start_frame = '<'
end_frame = '>'
count =0

while True:
	data = 'This is test message no: ' + str(count)
	#Create md5 check sum
	chksum = hashlib.md5(data).hexdigest()
	#Build message frame including some extraneous data and 
	message = "ignore_me" + start_frame + data +  chksum + end_frame + "and me"
	print "Sending message no: " + str(count)
#        while message:
#	    bytes = sock.send(message)
#	    buffer = message[bytes:]
	x = sock.send(message)
	count += 1
	sleep(1)
sock.close()
