#!/usr/bin/env python
# -*- coding: utf-8  -*-

def func_1(b, a = None):
	print(a)
	print(b)

def func_2(a = 1, *data):
	print(a)
	print(list(data))

if __name__ == "__main__":
	func_1(b = '123')
	func_2(20, 1,2,3,4)
	func_2(None, 1,2,3,4)
	func_2(None)
