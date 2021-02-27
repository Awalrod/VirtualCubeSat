#!/usr/bin/python3

import socket
import random
import math
import time
from PayloadTimer import PayloadTimer as pt

def sendPayload(conn):
	currentTime = time.time()
	battery = math.sin(currentTime*.00001)+1
	genericPayload1 = math.sin(currentTime*.0000001*random.randint(1,10))
	genericPayload2 = random.randint(0,100)
	message = '{"BATT":'+str(battery)+', "DATA1":'+str(genericPayload1)+', "DATA2":'+str(genericPayload2)+'}'
	print('Sending:'+message)
	s.sendall(message)

def main():
	HOST = '192.168.100.4'
	PORT = 55555


	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		#s.sendall(b'Hello, world')
		#data = s.recv(1024)
		payloadTimer = pt(5,sendPayload,s)
		while True:
			print("10 seconds")
			time.sleep(10)

	


main()