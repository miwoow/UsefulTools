#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class DialogSet(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'dialogset(对话框设置)'
        Table.sql = 'select * from dialogset'
        Table.titles = (u'对话框ID', u'内容')
        Table.__init__(self, cur, wb)
