#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Item(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'item(物品)'
        Table.sql = 'select * from item'
        Table.titles = (u'ID', u'名称', u'描述', u'图标路径', u'类型', u'效果ID', u'可叠加', u'bandAble', u'可丢弃throwAble', u'可使用', u'最多使用数', u'子类型', u'等级', u'颜色', u'卖价格', u'买价格', u'购买荣誉', u'购买联盟', u'荣誉类型', u'dropAble', u'instDesc', u'instCur', u'instMax', u'任务ID', u'time', u'gemValue', u'gemNeedNum(宝石)', u'nextGemLevelEntId', u'userHasMaxNum', u'useContent')
        Table.__init__(self, cur, wb)
