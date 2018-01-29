#!/usr/bin/env python
# -*- coding: utf-8  -*-

import unittest

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Sequence, MetaData
from sqlalchemy.orm import sessionmaker
import pandas as pd
import numpy as np

Base = declarative_base()
metadata = MetaData()

class LoadBatches(Base):
	__tablename__ = "loadbatches1"

	code = Column(String(50), nullable = True, primary_key = True)
	name = Column(String(50), nullable = True)
	desc = Column(String(200), nullable = True)
	create_date = Column(TIMESTAMP, nullable = True)

	def __repr__(self):
		return "<LoadBatches(code='%s', name='%s', desc='%s', create_date='%s')>" % \
			(self.code, self.name, self.desc, self.create_date)


class SqlAlchemyTest(unittest.TestCase):

	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_pygresql(self):
		import pg
		
		conn = pg.connect(dbname = 'testdb', host = '10.13.28.34', user = 'pgadmin', passwd = 'pgadmin.') 
		sql_select = "select * from base_users"
		users = conn.query(sql_select).dictresult()
		self.assertTrue(len(users) > 0)
		for row in users:
			print(row)
			
	def test_sqlalchemy_psycopg2(self):
		db_url = "postgresql+psycopg2://pgadmin:pgadmin.@localhost:5432/testdb"

		engine = create_engine(db_url, echo=True)

		tb = Table("test_table2", metadata, 
			 Column("name", String(100), nullable = True), 
			 Column("code", String(100), nullable = True),
			 Column("description", String(200), nullable = True),
			 schema = "test_schema")
		tb.metadata.bind = engine

		if not tb.exists():
			tb.create()

		#dict_batch1 = {"name": "test_batch_1","description": None}
		#dict_batch2 = {"name": None, "description": "DESCCCCCC"}
		df = pd.DataFrame(data = [["test_batch_2", np.nan, None], [None, np.nan, "DESCSSSSS"]], columns = ["name", "code", "description"])
		print(df)
		#df = df.fillna(method = lambda x: None if pd.isnull(x) else x)
		df = df.applymap(lambda x: None if pd.isnull(x) else x)

		engine.execute(tb.insert(),df.to_dict(orient = "records"))

		
		#result = connection.execute(text("select * from :tbl"),{'tbl': 'jd_sys.base_users'})
		##self.assertTrue(len(result) > 0)
		#for row in result:
		#	print(row)
		
	def test_sqlalchemy_pygresql(self):
		db_url = "postgresql+pygresql://pgadmin:pgadmin.@10.13.28.34:5432/testdb"

		engine = create_engine(db_url, echo=True)

		connection = engine.connect()

	def test_delcare_mapping(self):
		print(LoadBatches.__table__)
		lb1 = LoadBatches()
		lb1.code = "AAAAAA001"
		lb1.name = "batch01"
		lb1.desc = "DESC123"
		lb1.create_date = "2010-01-01"
		print(lb1)

		db_url = "postgresql+psycopg2://pgadmin:pgadmin.@localhost:5432/testdb"
		engine = create_engine(db_url, echo=True)
		Base.metadata.drop_all(engine)
		Base.metadata.create_all(engine)

		Session = sessionmaker(bind=engine)
		session = Session()
		session.add(lb1)
		session.commit()

	def test_table_existed(self):
		db_url = "postgresql+psycopg2://pgadmin:pgadmin.@localhost:5432/testdb"
		engine = create_engine(db_url, echo=True)
		lb = Table("loadbatches21", Base.metadata, autoload_with=engine, autoload = True)
		self.assertTrue(len(lb.columns) > 0)

		
		
def suite():
	suite = unittest.TestSuite()
	#suite.addTest(SqlAlchemyTest("test_pygresql"))
	suite.addTest(SqlAlchemyTest("test_sqlalchemy_psycopg2"))
	#suite.addTest(SqlAlchemyTest("test_delcare_mapping"))
	#suite.addTest(SqlAlchemyTest("test_table_existed"))
	return suite
	
if __name__ == "__main__":
	unittest.main(defaultTest = "suite")