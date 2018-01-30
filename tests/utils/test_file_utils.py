"""
execute the unittest file in project root directory.
"""
import sys
sys.path.insert(0, r"../datalet")

import os
import unittest

from tests.testing import Testing
import datalet.utils.file_utils as fus

class FileUtilsTesting(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_try_read_utf8(self):
		sql_ch_filepath = r"tests/test_data/sql_ch_utf8.sql"
		sql_text = fus.try_read(sql_ch_filepath)
		print(sql_text)

	def test_try_read_gb2312(self):
		sql_ch_filepath = r"tests/test_data/sql_ch_gb2312.sql"
		sql_text = fus.try_read(sql_ch_filepath)
		print(sql_text)

	# def test_get_exec_file_path(self):
	# 	print(fus.get_exec_file_path())

	def test_convert_encoding(self):
		saved_filepath = fus.convert_encoding(r"tests/test_data/sql_ch_gb2312.sql", inplace = False)
		encoding = fus.detect_charset(saved_filepath)["encoding"]
		self.assertTrue(encoding == "UTF-8")

	def test_convert_encoding_inplace(self):
		saved_filepath = fus.convert_encoding(r"tests/test_data/sql_ch_gb2312_inplace.sql", inplace = True)
		encoding = fus.detect_charset(saved_filepath)["encoding"]
		self.assertTrue(encoding == "UTF-8")
		fus.convert_encoding(saved_filepath, target_encoding = "gb2312")

def suite():
	suite = unittest.TestSuite()
	#suite.addTest(CsvStorageTest("test_create_file_not_exists"))
	#suite.addTest(CsvStorageTest("test_create_file_exists"))
	#suite.addTest(CsvStorageTest("test_create_file_exists_force"))
	suite.addTest(FileUtilsTesting("test_read_text_file_utf8"))
	suite.addTest(FileUtilsTesting("test_read_text_file_gb2312"))
	# suite.addTest(FileUtilsTesting("test_get_exec_file_path"))
	suite.addTest(FileUtilsTesting("test_convert_encoding"))
	suite.addTest(FileUtilsTesting("test_convert_encoding_inplace"))
	#suite.addTest(CsvStorageTest("test_copy"))
	#suite.addTest(CsvStorageTest("test_copy_path"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
