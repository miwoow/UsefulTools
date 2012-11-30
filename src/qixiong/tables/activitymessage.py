#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ActivityMessage(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'activitymessage(活动信息)'
        Table.sql = 'select * from activiymessage'
        Table.titles = (u'ID', u'类型', u'获胜次数', u'信息')
        Table.__init__(self, cur, wb)
