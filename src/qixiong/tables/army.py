#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

from table import Table

class Army(Table):
    def __init__(self, cur, wb):
        Table.sheet_name = u'army(军队)'
        Table.sql = 'select * from army'
        Table.titles = (u'ID', u'名称', u'描述', u'类型', u'图标路径', u'攻击', u'防御', u'敏捷', u'hp', u'等级', u'攻击类型', u'护甲类型', u'移动力，战场上每回合最远的移动距离', u'机动力，每回合兵种行动的先后顺序', u'搬运力，每个兵能携带的资源量', u'命中率', u'闪避率', u'暴击率', u'连击率', u'反击率', u'最大攻击距离，最小是1', u'进食')
        Table.__init__(self, cur, wb)
