#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class LvParaLimit(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'等级参数限制'
        Base.table_name = 'lvparalimit'
        Base.__init__(self, cur, wb)
