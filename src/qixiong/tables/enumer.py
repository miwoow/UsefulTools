#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Enumer(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'enumer(枚举)'
        Table.sql = 'select * from enumer'
        Table.titles = (u'编号', u'所属组', u'值', u'描述', u'顺序')
        Table.__init__(self, cur, wb)
