#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class Skill(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'技能'
        Base.table_name = 'skill'
        Base.__init__(self, cur, wb)
