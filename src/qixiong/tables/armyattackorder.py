#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ArmyAttackOrder(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'armyattackorder(军队攻击顺序)'
        Table.sql = 'select * from armyattackorder'
        Table.titles = (u'ID', u'攻击部队类型', u'防守部队类型', u'顺序')
        Table.__init__(self, cur, wb)
