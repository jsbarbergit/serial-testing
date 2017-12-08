import serial
import hashlib
from time import sleep

port = '/tmp/COM1'
ser = serial.Serial(port, 9600)
start_frame = '<'
end_frame = '>'
count =0

while True:
	data = 'This is test message no: ' + str(count)
	#Create md5 check sum
	chksum = hashlib.md5(data).hexdigest()
	#Build message frame including some extraneous data and 
	message = "ignore_me" + start_frame + data +  chksum + end_frame + "and me"
	x = ser.write(message)
	count += 1
	print "Sending message no: " + str(count)
	sleep(0.1)
ser.close()
