#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class GuildTechEffect(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'guildtecheffect(联盟科技效果)'
        Table.sql = 'select * from guildtecheffect'
        Table.titles = (u'ID', u'科技ID', u'科技等级', u'科技名称', u'效果名称', u'效果描述', u'图片路径', u'联盟Con', u'升次数', u'升级荣誉', u'依赖建筑', u'依赖建筑等级', u'依赖联盟等级', u'效果ID', u'参数1', u'参数2', u'参数3')
        Table.__init__(self, cur, wb)
