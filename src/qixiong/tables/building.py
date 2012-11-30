#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Building(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'building(建筑)'
        Table.sql = 'select * from building'
        Table.titles = (u'建筑ID', u'名称', u'描述', u'图标路径', u'数量限制', u'最高等级', u'属性', u'建筑类型')
        Table.__init__(self, cur, wb)
