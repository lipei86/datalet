#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import unittest

def test():

	tests_utils = unittest.TestLoader().discover('tests/utils')
	unittest.TextTestRunner(verbosity = 2).run(tests_utils)

	tests_storages = unittest.TestLoader().discover('tests/storage')
	unittest.TextTestRunner(verbosity = 2).run(tests_storages)

	tests_data = unittest.TestLoader().discover('tests/data')
	unittest.TextTestRunner(verbosity = 2).run(tests_data)


if __name__ == '__main__':
	test()
