#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

class Table:
    sheet_name = u'Table'
    sql = ''
    titles = ()
    def __init__(self, cur, wb):
        self.cur = cur
        self.wb = wb

    def genHead(self, ):
        self.ws = self.wb.add_sheet(Table.sheet_name)

        col_index = 0
        for t in Table.titles:
            self.ws.write(0, col_index, t)
            col_index += 1
        
    def doit(self, ):
        self.genHead()
        self.cur.execute(Table.sql)
        rows = self.cur.fetchall()
        
        row_index=1
        for row in rows:
            col_index=0
            for field in row:
                self.ws.write(row_index, col_index, field)
                col_index += 1
            row_index += 1
