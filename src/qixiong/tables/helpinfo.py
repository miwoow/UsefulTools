#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class HelpInfo(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'helpinfo(帮助信息)'
        Table.sql = 'select * from helpinfo'
        Table.titles = (u'ID', u'菜单ID', u'preOrder', u'内容', u'pic1', u'pic2', u'pic3', u'标题')
        Table.__init__(self, cur, wb)
