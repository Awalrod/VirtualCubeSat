#!/usr/bin/python3

import socket
import random
import math
import time
from PayloadTimer import PayloadTimer as pt

def sendPayload():
	currentTime = time.time()
	battery = math.sin(currentTime*.00001)+1
	genericPayload1 = math.sin(currentTime*.0000001*random.randint(1,10))
	genericPayload2 = random.randint(0,100)
	message = '{"BATT":'+str(battery)+', "DATA1":'+str(genericPayload1)+', "DATA2":'+str(genericPayload2)+'}'
	print(message)

def main():
	HOST = '127.0.0.1'	# The server's hostname or IP address
	PORT = 65432		# The port used by the server

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		#s.connect((HOST, PORT))
		#s.sendall(b'Hello, world')
		#data = s.recv(1024)
		payloadTimer = pt(5,sendPayload)
		while True:
			print("10 seconds")
			time.sleep(10)

	


main()