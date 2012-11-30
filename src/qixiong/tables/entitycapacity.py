#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class EntityCapacity(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'entitycapacity(建筑容量)'
        Table.sql = 'select * from entitycapacity'
        Table.titles = (u'编号', u'等级', u'容量', u'描述', u'参数1', u'参数2', u'图标路径', u'类型1', u'类型2')
        Table.__init__(self, cur, wb)
