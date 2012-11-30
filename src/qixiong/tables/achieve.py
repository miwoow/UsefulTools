#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Achieve(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'achieve(声望)'
        Table.sql = 'select * from achieve'
        Table.titles = (u'序号', u'名称', u'详情', u'类型', u'子类型', u'声望值', u'参数1', u'参数2', u'参数3', u'等级(成就在某一子类型中的等级)')
        Table.__init__(self, cur, wb)
