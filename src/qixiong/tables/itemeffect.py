#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ItemEffect(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'itemeffect(物品效果)'
        Table.sql = 'select * from itemeffect'
        Table.titles = (u'ID', u'beanName', u'para1', u'para2', u'para3', u'效果名称', u'效果描述', u'效果等级', u'图标路径', u'效果类型', u'子类类型', u'buffName')
        Table.__init__(self, cur, wb)
