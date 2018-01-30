#!/usr/bin/env python
# -*- coding: utf-8  -*-

"""
execute the unittest file in project root directory.
"""
import sys
sys.path.insert(0, r"../datalet")

from datalet.logging import *
import unittest
from tests.testing import Testing

class LoggerTesting(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_use_default_config(self):
		lgr = Logger()
		lgr.debug("debug message")
		lgr.info("info message")
		lgr.warning("warning message")
		lgr.error("error message")
		lgr.critical("critical message")


def suite():
	suite = unittest.TestSuite()
	suite.addTest(LoggerTesting("test_use_default_config"))
	#suite.addTest(LoggerTesting("test_iter"))
	#suite.addTest(LoggerTesting("test_to_dict"))
	#suite.addTest(LoggerTesting("test_append_row"))
	#suite.addTest(LoggerTesting("test_get_data_by_column"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
