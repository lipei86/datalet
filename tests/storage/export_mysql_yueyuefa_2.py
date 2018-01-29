#!/usr/bin/env python
# -*- coding: utf-8  -*-

"""
execute the unittest file in project root directory.
"""
import sys
sys.path.insert(0, r"../datalet")

import unittest

import pandas as pd

from datalet.data import *
from datalet.storage import *
from datalet.storage.dbtable_storage import *
import datalet.storage.facade as sfd
from sqlalchemy import create_engine

mysql_db_url = create_mysql_dburl("localhost", "abc", "abc", "123456", port = 8866)
engine = create_engine(mysql_db_url)

#sql_yueyuefa = "" \
# " select * from (" \
# " select ap.id, ap.uid, ap.corp, cb.status, ap.fund, ap.refund, cb.paidprincipal, cb.principal, cb.paidinterest, cb.interest, ap.applytime, ap.canceltime, ap.period, ap.applyuid, cb.beginday, cb.endday from adv_payment ap left join credit_bill cb on ap.id = cb.advid" \
# " union" \
# " select ap.id, ap.uid, ap.corp, cb.status, ap.fund, ap.refund, cb.paidprincipal, cb.principal, cb.paidinterest, cb.interest, ap.applytime, ap.canceltime, ap.period, ap.applyuid, cb.beginday, cb.endday from adv_payment ap left join credit_bill cb on ap.id = cb.advid" \
# " ) full_table "
sql_yueyuefa = "" \
" select ai.acct_name, ai.filter_company_name, ai.trade1_name, ai.trade2_name, ap.*, year(ap.applytime) as apply_year " \
" from yueyuefa.adv_payment ap " \
" left join yueyuefa.ods_fc_acct_info ai on ap.uid = ai.acct_id " \

result = engine.execute(text(sql_yueyuefa), {})
ret_all = result.fetchall()
#first = ret_all[:5]
#print(first)

dt_yueyuefa = DataTable("table_yueyuefa",
	DataColumn(name = "id", caption = "信用加款流水号"),
	DataColumn(name = "uid", caption = "账户ID"),
	DataColumn(name = "acct_name", caption = "账户名称"),
	DataColumn(name = "filter_company_name", caption = "客户公司名称"),
	DataColumn(name = "trade1_name", caption = "一级行业"),
	DataColumn(name = "trade2_name", caption = "二级行业"),
	DataColumn(name = "corp", caption = "所属分公司"),
	DataColumn(name = "status", caption = "当前支付状态"),
	DataColumn(name = "fund", caption = "信用加款金额"),
	DataColumn(name = "refund", caption = "信用退款金额"),

	DataColumn(name = "applytime", caption = "信用加款时间"),
	DataColumn(name = "canceltime", caption = "还款截止时间"),
	DataColumn(name = "period", caption = "授信账期"),
	DataColumn(name = "applyuid", caption = "申请客服"),
	DataColumn(name = "apply_year", caption = "信用加款年份"))

for row in ret_all:
	dt_yueyuefa.append(dict(row))

print(len(dt_yueyuefa))

sfd.write_file(r"D:\yueyuefa_acct.xlsx", data = dt_yueyuefa, sheetIndex = 0, force = True, overwrite=True)

# es_yueyuefa = sfd.create_file(r"D:\yueyuefa.xlsx", sheetIndex = 0, force = True)
# if es_yueyuefa.exists_file():
	# es_yueyuefa.remove()
# es_yueyuefa.write(data = dt_yueyuefa)
