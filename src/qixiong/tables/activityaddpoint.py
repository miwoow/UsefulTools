#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ActivityAddPoint(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'activityaddpoint(活跃度计算)'
        Table.sql = 'select * from activityaddpoint'
        Table.titles = (u'序号', u'活跃度计算项目', u'增加数量描述(5+10+15)', u'完成次数', u'增加数量')
        Table.__init__(self, cur, wb)
