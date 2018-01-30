#!/usr/bin/env python
# -*- coding: utf-8  -*-

"""
execute the unittest file in project root directory.
"""
import sys
sys.path.insert(0, r"../datalet")

from datalet.data import *
import unittest

class DataRowTesting(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_init(self):
		ls = ['zhangsan', 20, 'abc@abc.com']
		dr = DataRow(None, ls)
		self.assertTrue(dr[0] == 'zhangsan')

	def test_get_data_by_colname(self):
		dt = DataTable(name = None, columns = ['name', 'age', 'email'])
		ls = ['zhangsan', 20, 'abc@abc.com']
		dr = DataRow(dt, ls)
		self.assertTrue(dr['name'] == 'zhangsan')
