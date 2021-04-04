#!/usr/bin/python3
import sys
import socket
import random
import math
import time
from PayloadTimer import PayloadTimer as pt
from reedsolo import RSCodec, ReedSolomonError

rsc = RSCodec(32) 
s = None

def sendPayload(conn):
	currentTime = time.time()
	battery = math.sin(currentTime*.00001)+1
	genericPayload1 = math.sin(currentTime*.0000001*random.randint(1,10))
	genericPayload2 = random.randint(0,100)
	message = '{"BATT":'+str(battery)+', "DATA1":'+str(genericPayload1)+', "DATA2":'+str(genericPayload2)+'}'
	print('Sending:'+message)
	encodedMsg = rsc.encode(str.encode(message))
	conn.sendall(encodedMsg)

def main():
	HOST = sys.argv[1]
	PORT = int(sys.argv[2])

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	#s.sendall(b'Hello, world')
	#data = s.recv(1024)
	payloadTimer = pt(2,sendPayload,s)
	


main()