class ClassA(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.__mymethod(a)

	def __mymethod(self, x):
		print("haha: %d" % x)


if __name__ == "__main__":
	c = ClassA(a = 1, b=3)
