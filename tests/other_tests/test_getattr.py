#!/usr/bin/env python
# -*- coding: utf-8  -*-

class Student(object):

	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		self.__tabledata = {'email': 'abc@abc.com', 'age': 20}

	@property
	def name(self):
		return self.__name

	@property
	def age(self):
		return self.__age

	def __getattr__(self, attrname):
		"""
		如果attrname在类中已经有定义，则调用类中属性。
		"""
		if attrname in self.__tabledata:
			return self.__tabledata[attrname]
		else:
			return None

if __name__ == "__main__":
	s = Student(name = "zhangsan", age = 101)
	print(s.name)
	print(s.email)
	print(s.age)
