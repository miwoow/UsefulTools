#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class HeroXuanYan(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'heroxuanyan(英雄宣言)'
        Table.sql = 'select * from heroxuanyan'
        Table.titles = (u'ID', u'chartr', u'内容', u'类型')
        Table.__init__(self, cur, wb)
