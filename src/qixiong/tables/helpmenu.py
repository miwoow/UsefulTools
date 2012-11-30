#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class HelpMenu(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'helpmenu(帮助菜单)'
        Table.sql = 'select * from helpmenu'
        Table.titles = (u'ID', u'名称', u'uri', u'父ID', u'关键字')
        Table.__init__(self, cur, wb)
