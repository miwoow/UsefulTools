#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class BoxAward(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'boxaward(宝箱奖励)'
        Table.sql = 'select * from boxaward'
        Table.titles = (u'ID', u'宝箱ID', u'宝箱名称', u'奖励名称', u'类型', u'对象ID', u'对象数量', u'重量', u'图标路径', u'是否需要将消息发送到世界频道(1,需要;0,不需要)', u'发送至世界频道的消息')
        Table.__init__(self, cur, wb)
