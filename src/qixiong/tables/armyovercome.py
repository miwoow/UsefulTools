#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ArmyOvercome(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'armyovercome(军队相克参数)'
        Table.sql = 'select * from armyovercome'
        Table.titles = (u'ID', u'攻击军队类型', u'防守军队类型', u'因子')
        Table.__init__(self, cur, wb)
