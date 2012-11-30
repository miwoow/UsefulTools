#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class DailyMission(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'dailymission(每日任务)'
        Table.sql = 'select * from dailymission'
        Table.titles = (u'序号', u'图标路径', u'名称', u'任务描述', u'详情', u'需要用户属性', u'需要用户值', u'需要活跃值', u'活动时间', u'增加用户荣誉', u'增加用户点数最小值', u'增加用户点数中间值', u'增加用户点数最大值', u'粮食', u'金钱', u'空闲Pop', u'新军队', u'塔兵数量', u'掉落包裹ID', u'成果最小', u'成果适中', u'成果最大', u'冷却时间', u'rank id')
        Table.__init__(self, cur, wb)
