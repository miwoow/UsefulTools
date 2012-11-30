#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ActivityBox(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'activitybox(声望宝箱)'
        Table.sql = 'select * from activitybox'
        Table.titles = (u'序号', u'宝箱ID', u'宝箱数量', u'需求的活跃度')
        Table.__init__(self, cur, wb)
