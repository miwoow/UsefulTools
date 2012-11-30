#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class Mission(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'任务'
        Base.table_name = 'mission'
        Base.__init__(self, cur, wb)
