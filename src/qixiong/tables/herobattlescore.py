#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class HeroBattleScore(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'herobattlescore(英雄战斗得分)'
        Table.sql = 'select * from herobattlescore'
        Table.titles = (u'分数', u'描述', u'itemNum')
        Table.__init__(self, cur, wb)
