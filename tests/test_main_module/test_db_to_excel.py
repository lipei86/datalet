#!/usr/bin/env python
# -*- coding: utf-8  -*-
import sys
sys.path.insert(0, r"../datalet")

import datalet.utils.sql_utils as sql_utils
from datalet.storage.excel_storage import ExcelStorage
from datalet.data import *

from sqlalchemy import create_engine, text


db_url = sql_utils.create_pgsql_sqlalchemy_dburl('localhost', 'foodmartdb', 'db_admin', 'db_admin')
excel_fact_location = "D:\\sales_fact_1998.xlsx"
excel_dim_store_location = "D:\\store.xlsx"
excel_dim_product_location = "D:\\product.xlsx"
excel_dim_product_class_location = "D:\\product_class.xlsx"

engine = create_engine(db_url)

# fact 1998
sql_select_fact_1998 = "select * from public.sales_fact_1998"
result = engine.execute(text(sql_select_fact_1998), {})
ret_all = result.fetchall()
dt_fact = DataTable("fact_1998", columns = ['product_id', 'time_id', 'customer_id', 'promotion_id', 'store_id', 'store_sales', 'store_cost', 'unit_sales'])
for row in ret_all:
	dt_fact.append(dict(row))
print(len(dt_fact))
fact_stg = ExcelStorage(location = excel_fact_location)
fact_stg.write(data = dt_fact, force = True, overwrite = True)


# store
sql_select_sotre = "select * from public.store"
result = engine.execute(text(sql_select_sotre), {})
ret_all = result.fetchall()
dt_store = DataTable("store", columns = ['store_id', 'store_type', 'region_id', 'store_name', 'store_city', 'store_state', 'store_country'])
for row in ret_all:
	dt_store.append(dict(row))
print(len(dt_store))
store_stg = ExcelStorage(location = excel_dim_store_location)
store_stg.write(data = dt_store, force = True, overwrite = True)


# product
sql_select_product = "select * from public.product"
result = engine.execute(text(sql_select_product), {})
ret_all = result.fetchall()
dt_product = DataTable("product", columns = ['product_id', 'product_name', 'brand_name', 'product_class_id'])
for row in ret_all:
	dt_product.append(dict(row))
print(len(dt_product))
product_stg = ExcelStorage(location = excel_dim_product_location)
product_stg.write(data = dt_product, force = True, overwrite = True)


# product class
sql_select_product_class = "select * from public.product_class"
result = engine.execute(text(sql_select_product_class), {})
ret_all = result.fetchall()
dt_product_class = DataTable("product_class", columns = ['product_class_id', 'product_subcategory', 'product_category', 'product_department', 'product_family'])
for row in ret_all:
	dt_product_class.append(dict(row))
print(len(dt_product_class))
product_class_stg = ExcelStorage(location = excel_dim_product_class_location)
product_class_stg.write(data = dt_product_class, force = True, overwrite = True)
