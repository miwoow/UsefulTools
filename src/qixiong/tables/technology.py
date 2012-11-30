#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class Technology(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'科技'
        Base.table_name = 'technology'
        Base.__init__(self, cur, wb)
