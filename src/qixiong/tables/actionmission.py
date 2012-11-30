#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class ActionMission(Table):

    def __init__(self, cur, wb):
        Table.sheet_name = u'actionmission(活动任务)'
        Table.sql = 'select * from actionmission'
        Table.titles = (u'任务ID', u'名称', u'活动时间(|分隔开始和结束时间)', u'活动描述', u'规则', u'目标描述(描述1|描述2|描述3)', u'参数1', u'参数2', u'参数3', u'脚本名', u'奖励道具(道具ID,数量;道具ID,数量;)', u'是否展现(0-不展现,1-展现', u'任务面板内显示的任务名')
        Table.__init__(self, cur, wb)

