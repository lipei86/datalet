
def callee(name, age, sex, addr = "Beijing"):
	print("name: ", name, ", age: ", age, ", sex: ", sex, ", addr: ", addr)

def caller(name, sex = "boy", **kwargs):
	callee(name, sex = sex, **kwargs)

def sum(start, *numbers):
	ret = start
	for n in numbers:
		ret += n
	return ret

class Calcator(object):
	def __init__(self, start, *numbers):
		self.start = start
		self.numbers = numbers
		self.__start = start
		print("__start: %d" % self.__start)
		print(self.start)
		print(self.numbers)

	def sum(self):
		ret = self.start
		for n in self.numbers:
			ret += n
		return ret

class Start(object):
	def getdata(self):
		return 27

class Calcator(object):

	def __init__(self, start, *numbers):
		self.start = start
		self.numbers = numbers
		self.__start = start
		print(self.__start)
		print(self.start)
		print(self.numbers)

	def sum(self):
		ret = self.start.getdata()
		for n in self.numbers:
			ret += n
		return ret

if __name__ == "__main__":
	kwargs = {"age": 30, "addr": "Guangzhou"}
	caller("zhangsan", **kwargs)
	print(sum(10, 1,2,3,4,5))
	c = Calcator(Start(), 1,2,3,4,5)
	print(c.sum())