#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class LuckTip(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'运气提示'
        Base.table_name = 'lucktip'
        Base.__init__(self, cur, wb)

