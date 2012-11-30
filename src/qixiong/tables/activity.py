#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Activity(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'activity(活动)'
        Table.sql = 'select * from activity'
        Table.titles = (u'活动ID(活跃度计算项目)', u'活跃度项目描述', u'完成最大值', u'完成单位(个,次,万)', u'奖励提示')
        Table.__init__(self, cur, wb)
