#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Event(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'event(事件)'
        Table.sql = 'select * from event'
        Table.titles = (u'事件ID', u'actNum', u'发送邮件', u'邮件标题', u'邮件内容', u'发送聊天消息', u'消息内容', u'频道', u'子频道', u'sendWin', u'winStartId', u'sendPChat', u'chatP内容', u'chatPChannel', u'chatPChildChannel')
        Table.__init__(self, cur, wb)
