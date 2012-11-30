#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Guide(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'guide(引导)'
        Table.sql = 'select * from guide'
        Table.titles = (u'引导ID', u'下一引导ID', u'回复1', u'回复2', u'回复脚本1', u'回复脚本2', u'场景名称', u'显示类型', u'图片地址', u'X', u'Y', u'点', u'关闭条件', u'关闭引导ID', u'内容', u'标题', u'位置')
        Table.__init__(self, cur, wb)
