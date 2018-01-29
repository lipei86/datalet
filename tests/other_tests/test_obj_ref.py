
class Parent(object):
	
	def __init__(self, name):
		self.__name = name
		self.children = []

	@property
	def name(self):
		return self.__name

	def add_child(self, childdata):
		c = Child(self,childdata)
		self.children.append(c)

	def __iter__(self):
		return iter(self.children)

class Child():
	def __init__(self, parent, data):
		self.__parent = parent
		self.__data = data

	@property
	def parent(self):
		return self.__parent

	@parent.setter
	def parent(self, value):
		self.__parent = value

	def get_data(self):
		return self.__data


if __name__ == "__main__":
	p = Parent("PPPP")
	#c = Child()
	p.add_child(8)
	#print()
	for c in p:
		print(c.parent.name)
		print(c.get_data())