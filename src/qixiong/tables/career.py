#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Career(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'career(职业)'
        Table.sql = 'select * from career'
        Table.titles = (u'职业ID', u'职业名称', u'职业能力名称', u'步兵', u'工兵', u'车兵', u'骑兵', u'器械')
        Table.__init__(self, cur, wb)
