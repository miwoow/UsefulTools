#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class Resource(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'资源'
        Base.table_name = 'resource'
        Base.__init__(self, cur, wb)
