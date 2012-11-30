#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ActionTip(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'actiontip(活动提示)'
        Table.sql = 'select * from actiontip'
        Table.titles = (u'名称', u'显示名称', u'活动描述', u'奖励描述', u'类型', u'战斗类型')
        Table.__init__(self, cur, wb)

