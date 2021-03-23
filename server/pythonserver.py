#!/usr/bin/python3

import socket
import threading

class GroundServer:
	def __init__(self,ip,port,callback):
		self.HOST = ip #'192.168.100.4'
		self.PORT = port #55555
		self.callback = callback
		self.connThreads = []
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.bind((self.HOST,self.PORT))
		self.isListening=False;
	
	def startServer(self):
		if(not self.isListening):
			print("Opening socket "+self.HOST+":"+str(self.PORT))
			self.listenerThread = threading.Thread(target=self.getConnections,daemon=True)
			self.isListening=True;
			self.listenerThread.start()
		
	def getConnections(self):
		print("Listening for incoming connections on "+self.HOST+":"+str(self.PORT))
		try:
			while (self.isListening) :
				self.sock.listen()
				conn,addr=self.sock.accept()
				print("Inoming connection from "+addr[0]+":"+str(addr[1]))
				newThread = WorkerThread(conn=conn,addr=addr,callback=self.callback)
				self.connThreads.append(newThread)
				newThread.start()
		finally:
			self.sock.close()
			
	def quit(self):
		for connThread in self.connThreads:
			connThread.stopThread()
		self.isListening=False
			


class WorkerThread(threading.Thread):
	def __init__(self, group=None, target=None, name=None, conn=None, addr=None, callback=None):
		super(WorkerThread,self).__init__(group=group, target=target, name=name)
		self.conn = conn
		self.addr = addr
		self.callback = callback
		self.isListening = True
		return
		
	def stopThread(self):
		self.isListening = False
		
	def run(self):
		try:
			while self.isListening:
				data = self.conn.recv(1024)
				if not data:
					break
				if self.callback and self.isListening:
					self.callback(data)
		finally:
			self.conn.close()