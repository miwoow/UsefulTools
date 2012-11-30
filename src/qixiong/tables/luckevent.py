#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class LuckEvent(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'luckevent(运气事件)'
        Table.sql = 'select * from luckevent'
        Table.titles = (u'事件ID', u'事件等级', u'事件类型', u'事件名称', u'事件描述', u'第一步', u'第二步', u'needResId', u'needResNum', u'奖励食物', u'奖励木材', u'奖励青铜', u'奖励金钱', u'awardPop', u'awardNewArmy', u'奖励荣誉', u'奖励经验值', u'awardProPoint', u'awardCasRange', u'奖励石料', u'图标路径', u'结果坏', u'结果一般', u'结果好', u'结果很好', u'是否在重建状态恢复繁荣度（0,否;1,是）')
        Table.__init__(self, cur, wb)
