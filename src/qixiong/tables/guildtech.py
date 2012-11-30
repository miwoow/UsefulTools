#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class GuildTech(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'guildtech(联盟科技)'
        Table.sql = 'select * from guildtech'
        Table.titles = (u'科技ID', u'科技名称', u'科技描述', u'图片路径', u'最高等级')
        Table.__init__(self, cur, wb)
