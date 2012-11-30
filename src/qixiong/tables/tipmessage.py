#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class TipMessage(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'提示信息'
        Base.table_name = 'tipmessage'
        Base.__init__(self, cur, wb)
