#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class AwardLuckFactor(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'awardluckfactor(奖励运气因子)'
        Table.sql = 'select * from awardluckfactor'
        Table.titles = (u'ID', u'运气名称', u'运气描述', u'因子', u'提示信息', u'图标')
        Table.__init__(self, cur, wb)

