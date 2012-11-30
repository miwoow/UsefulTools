#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

class Base:
    sheet_name = u'Base'
    table_name = u''
    def __init__(self, cur, wb):
        self.cur = cur
        self.wb = wb
        self.titles = []

    def genTitles(self, ):
        self.cur.execute("select column_name from information_schema.columns where table_name='%s'" % (Base.table_name,))
        rows = self.cur.fetchall()
        for row in rows:
            self.titles.append(row[0])


    def genHead(self, ):
        self.genTitles()
        self.ws = self.wb.add_sheet("%s(%s)" % (Base.table_name, Base.sheet_name))

        col_index = 0
        for t in self.titles:
            self.ws.write(0, col_index, t)
            col_index += 1
        
    def doit(self, ):
        self.genHead()
        sql = "select * from %s" % (Base.table_name, )
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        
        row_index=1
        for row in rows:
            col_index=0
            for field in row:
                self.ws.write(row_index, col_index, field)
                col_index += 1
            row_index += 1
