#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class GuildBui(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'guildbui(联盟建筑)'
        Table.sql = 'select * from guildbui'
        Table.titles = (u'建筑ID', u'名称', u'描述', u'最高等级', u'图片路径')
        Table.__init__(self ,cur, wb)
