#!/usr/bin/env python
# -*- coding: utf-8  -*-

from py4j.java_gateway import JavaGateway

def lanuch_gateway():
	pass

gateway = JavaGateway()
addi_app = gateway.entry_point
ret = addi_app.run_mdx("abc")
print(ret)