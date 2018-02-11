class Fibonacci():
	"""docstring for Fibonacci"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def fibGen(self):
		while True:
			yield  self.x
			self.x, self.y = self.y, self.x + self.y

fibObj = Fibonacci(1,1)

for i in fibObj.fibGen():
	if i > 100: break
	print(i, end=' ')