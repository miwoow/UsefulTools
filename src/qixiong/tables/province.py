#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class Province(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'城市'
        Base.table_name = 'province'
        Base.__init__(self, cur, wb)
