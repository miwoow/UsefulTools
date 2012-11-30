#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class HeroBattleStage(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'herobattlestage(英雄战斗场景)'
        Table.sql = 'select * from herobattlestage'
        Table.titles = (u'ID', u'战斗ID', u'场景顺序', u'名称', u'isBoss', u'场景描述', u'难度', u'pveCastleID')
        Table.__init__(self, cur, wb)
