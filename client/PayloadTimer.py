from threading import Timer

class PayloadTimer(object):
	def __init__(self, interval, function,conn):
		self._timer		= None
		self.interval	= interval
		self.function	= function
		self.conn 		= conn
		self.is_running = False
		self.start()

	def _run(self):
		self.is_running = False
		self.start()
		self.function(conn)

	def start(self):
		if not self.is_running:
			self._timer = Timer(self.interval, self._run)
			self._timer.start()
			self.is_running = True

	def stop(self):
		self._timer.cancel()
		self.is_running = False
		