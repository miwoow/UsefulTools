#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class EventWindow(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'eventwindow(事件窗口)'
        Table.sql = 'select * from eventwindow'
        Table.titles = (u'窗口ID', u'下个窗口ID', u'显示类型', u'回答', u'回复脚本', u'图片地址', u'内容')
        Table.__init__(self, cur, wb)
