#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class HeroBattle(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'herobattle(英雄战斗)'
        Table.sql = 'select * from herobattle'
        Table.titles = (u'ID', u'名称', u'描述', u'recomLevel', u'打开条件', u'地点')
        Table.__init__(self, cur, wb)
