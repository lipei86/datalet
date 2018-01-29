"""
execute the unittest file in project root directory.
"""
import sys
sys.path.insert(0, r"../datalet")

import os
import unittest

from tests.testing import Testing
import datalet.utils.datetime_utils as datetime_utils

class DatetimeUtilsTesting(Testing):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_get_week_date_range(self):
		date_val = '2017-07-07'
		for n in range(1,8):
			print('\nstart day: %d' % n)
			d_range = datetime_utils.get_week_date_range(date_val, start_weekday = n)
			print(d_range)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(DatetimeUtilsTesting("test_get_week_date_range"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
