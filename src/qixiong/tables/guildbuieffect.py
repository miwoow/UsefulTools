#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class GuildBuiEffect(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'guildbuieffect(联盟建筑效果)'
        Table.sql = 'select * from guildbuieffect'
        Table.titles = (u'ID', u'建筑ID', u'建筑等级', u'建筑名称', u'效果名称', u'效果描述', u'图片路径', u'建筑Con', u'升级次数', u'升级荣誉', u'依赖建筑ID', u'依赖建筑等级', u'依赖联盟等级', u'效果ID', u'参数1', u'参数2', u'参数3')
        Table.__init__(self, cur, wb)
