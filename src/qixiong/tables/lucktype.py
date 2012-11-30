#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class LuckType(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'运气类型'
        Base.table_name = 'lucktype'
        Base.__init__(self, cur, wb)
