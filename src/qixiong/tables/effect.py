#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Effect(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'effect(效果)'
        Table.sql = 'select * from effect'
        Table.titles = (u'效果ID', u'效果名称', u'效果说明', u'显示标志', u'装备效果图顺序')
        Table.__init__(self, cur, wb)
