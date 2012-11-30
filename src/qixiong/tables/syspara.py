#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class SysPara(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'系统参数'
        Base.table_name = 'syspara'
        Base.__init__(self, cur, wb)
