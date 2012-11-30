#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from base import Base

class Person(Base):
    def __init__(self, cur, wb):
        Base.sheet_name = u'人物'
        Base.table_name = 'person'
        Base.__init__(self, cur, wb)
