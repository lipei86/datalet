"""
execute the unittest file in project root directory.
"""
import sys
sys.path.insert(0, r"../datalet")

import os
import unittest

from tests.testing import Testing
import datalet.utils.datetime_utils as datetime_utils
import datetime

class DatetimeUtilsTesting(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_get_week_date_range(self):
		date_val = '2018-01-03'

		start_dates = []
		for start_weekday in range(1,8):
			d_range = datetime_utils.get_week_date_range(date_val, start_weekday = start_weekday)
			start_dates.append(d_range[0])
		self.assertTrue(start_dates[0] == datetime.date(2018, 1, 1))
		self.assertTrue(start_dates[1] == datetime.date(2018, 1, 2))
		self.assertTrue(start_dates[2] == datetime.date(2018, 1, 3))
		self.assertTrue(start_dates[3] == datetime.date(2017, 12, 28))
		self.assertTrue(start_dates[4] == datetime.date(2017, 12, 29))
		self.assertTrue(start_dates[5] == datetime.date(2017, 12, 30))
		self.assertTrue(start_dates[6] == datetime.date(2017, 12, 31))

def suite():
	suite = unittest.TestSuite()
	suite.addTest(DatetimeUtilsTesting("test_get_week_date_range"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
