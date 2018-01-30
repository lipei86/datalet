#!/usr/bin/env python
# -*- coding: utf-8  -*-

import sys
sys.path.insert(0, r"../actlet")

import os
import unittest

from actlet.olap import *
from tests.testing import Testing
from py4j.java_gateway import JavaGateway, GatewayParameters

class ClientTesting(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_ping(self):
		clt = Client()
		ret = clt.ping("abc")
		self.assertTrue(ret == "your msg:abc")
		#except Exception as err:
		#	raise err
		#finally:
		#	# shutdown() can close the server gateway.
		#	#gateway.shutdown()
		#	pass

	def test_mondrian_connect(self):
		cur_dir = os.path.split(os.path.realpath(__file__))[0]
		clt = Client()
		olap_driver = "mondrian.olap4j.MondrianOlap4jDriver"
		olap_url = "jdbc:mondrian:Jdbc=%s" % ("jdbc:postgresql://localhost:5432/foodmartdb")
		olap_catalog = os.path.join(cur_dir, "FoodMart.xml")
		olap_mdx = "SELECT {Measures.[Unit Sales]} ON COLUMNS FROM [Sales]"
		db_driver = "org.postgresql.Driver"
		db_username = "db_user"
		db_userpwd = "db_user"
		ret = clt.query_by_mdx(
			olap_driver = olap_driver,
			olap_url = olap_url,
			olap_catalog = olap_catalog,
			olap_mdx = olap_mdx,
			db_driver = db_driver,
			db_username = db_username,
			db_userpwd = db_userpwd)
		print(ret)




def suite():
	suite = unittest.TestSuite()
	suite.addTest(ClientTesting("test_ping"))
	suite.addTest(ClientTesting("test_mondrian_connect"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
