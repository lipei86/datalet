"""
execute the unittest file in project root directory.
"""
import sys
sys.path.insert(0, r"../datalet")

import os
import unittest

from tests.testing import Testing
import datalet.utils.list_utils as list_utils

class ListUtilsTesting(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_split_by_group_count(self):
		ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		groups = list_utils.split_by_group_count(ls, group_count = 3)
		print(groups)
		self.assertTrue(len(groups) == 3)

	def test_split_by_group_count_2(self):
		ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		groups = list_utils.split_by_group_count(ls, group_count = 3)
		print(groups)
		self.assertTrue(len(groups) == 3)

	def test_split_by_group_count_3(self):
		ls = [1, 2]
		groups = list_utils.split_by_group_count(ls, group_count = 3)
		print(groups)
		self.assertTrue(len(groups) == 1)

	def test_split_by_group_size(self):
		ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		groups = list_utils.split_by_group_size(ls, group_size = 3)
		print(groups)
		self.assertTrue(len(groups) == 4)

	def test_split_by_group_size_2(self):
		ls = [1, 2, 3]
		groups = list_utils.split_by_group_size(ls, group_size = 3)
		print(groups)
		self.assertTrue(len(groups) == 1)

	def test_split_by_group_size_3(self):
		ls = [1, 2]
		groups = list_utils.split_by_group_size(ls, group_size = 3)
		print(groups)
		self.assertTrue(len(groups) == 1)


def suite():
	suite = unittest.TestSuite()
	#suite.addTest(CsvStorageTest("test_create_file_not_exists"))
	#suite.addTest(CsvStorageTest("test_create_file_exists"))
	#suite.addTest(CsvStorageTest("test_create_file_exists_force"))
	suite.addTest(ListUtilsTesting("test_split_by_group_count"))
	suite.addTest(ListUtilsTesting("test_split_by_group_count_2"))
	suite.addTest(ListUtilsTesting("test_split_by_group_count_3"))
	suite.addTest(ListUtilsTesting("test_split_by_group_size"))
	suite.addTest(ListUtilsTesting("test_split_by_group_size_2"))
	suite.addTest(ListUtilsTesting("test_split_by_group_size_3"))
	# suite.addTest(FileUtilsTesting("test_read_text_file_gb2312"))
	# suite.addTest(FileUtilsTesting("test_get_exec_file_path"))
	# suite.addTest(FileUtilsTesting("test_convert_encoding"))
	# suite.addTest(FileUtilsTesting("test_convert_encoding_inplace"))
	#suite.addTest(CsvStorageTest("test_copy"))
	#suite.addTest(CsvStorageTest("test_copy_path"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
