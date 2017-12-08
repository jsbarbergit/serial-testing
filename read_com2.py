import serial
import hashlib
from time import sleep

port = "/tmp/COM2"
ser = serial.Serial(port, 9600, timeout=0)

start_frame = '<'
end_frame = '>'
hash_len = 32
escape_char='\\'

while True:
    state = "WAIT_FOR"
    print state
    data = ser.read(256)
    #There is some data
    if len(data) > 0:
        state = 'RECV'
        msg_str = ''
        print state
        count = 0
        for _char in data:
            if _char == start_frame:
                # Was this escaped? if so just add char
                if data[count - 1] == escape_char:
                    msg_str = msg_str + _char
                else:
                    #Genuine Start frame char rec'd
                    state = 'START_FRAME'
                    print state
            elif _char == end_frame:
                # Was this escaped? if so just add char
                if data[count - 1] == escape_char:
                    #Replace that escape char in the msg str with this one
                    msg_str = msg_str + _char
                else:
                    state = 'END_FRAME'
                    print state
                    #Actual msg is all chars from start to end minus hash length
                    message = msg_str[:len(msg_str) - hash_len]
                    chksum = msg_str[len(msg_str) - hash_len:]  
                    #Calculate our checksum
                    msg_chksum = hashlib.md5(message).hexdigest()
                    if msg_chksum == chksum:
                        print "Message Recd & Checked: " + message
                    else:   
                        print "ERROR - Unable to verify message: " + message
                    #Reset msg string in case there are more frames in this buffer
                    msg_str = ''
            else:
                #Are we in frame
                if state == 'START_FRAME':
                    msg_str = msg_str + _char
            count += 1
        print "Total Frames Received: " + str(count)
    sleep(0.1)
    print state

ser.close()
