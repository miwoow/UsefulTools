#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

import MySQLdb as mdb
import xlwt
from datetime import datetime

from tables import *
#from tables.achieve import Achieve
#from tables.actionmission import ActionMission

font0 = xlwt.Font()
font0.name = '宋体'
font0.olour_index = 2
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

wb = xlwt.Workbook()

try:
    conn = mdb.connect('localhost', 'root', '123', 'dynasty', charset='utf8')

    cur = conn.cursor()

    achieve = Achieve(cur, wb)
    achieve.doit()

    actionmission  = ActionMission(cur, wb)
    actionmission.doit()

    activitymessage = ActivityMessage(cur, wb)
    activitymessage.doit()

    awardluckfactor = AwardLuckFactor(cur, wb)
    awardluckfactor.doit()

    activity = Activity(cur, wb)
    activity.doit()

    boxaward = BoxAward(cur, wb)
    boxaward.doit()

    actiontip = ActionTip(cur, wb)
    actiontip.doit()

    armyattackorder = ArmyAttackOrder(cur, wb)
    armyattackorder.doit()

    activityaddpoint = ActivityAddPoint(cur, wb)
    activityaddpoint.doit()

    armyovercome = ArmyOvercome(cur, wb)
    armyovercome.doit()

    activitybox = ActivityBox(cur, wb)
    activitybox.doit()

    army = Army(cur, wb)
    army.doit()

    building = Building(cur, wb) 
    building.doit()

    career = Career(cur, wb)
    career.doit()

    dailymission = DailyMission(cur, wb)
    dailymission.doit()

    dialogset = DialogSet(cur, wb)
    dialogset.doit()

    effect = Effect(cur, wb)
    effect.doit()

    entitycapacity = EntityCapacity(cur, wb)
    entitycapacity.doit()

    enumer = Enumer(cur, wb)
    enumer.doit()

    event = Event(cur, wb)
    event.doit()

    eventwindow = EventWindow(cur, wb)
    eventwindow.doit()

    guide = Guide(cur, wb)
    guide.doit()

    guildbui = GuildBui(cur, wb)
    guildbui.doit()

    guildbuieffect = GuildBuiEffect(cur, wb)
    guildbuieffect.doit()

    guildtech = GuildTech(cur, wb)
    guildtech.doit()

    guildtecheffect = GuildTechEffect(cur, wb)
    guildtecheffect.doit()

    helpinfo = HelpInfo(cur, wb)
    helpinfo.doit()

    helpmenu = HelpMenu(cur, wb)
    helpmenu.doit()

    herobattle = HeroBattle(cur, wb)
    herobattle.doit()

    herobattlescore = HeroBattleScore(cur, wb)
    herobattlescore.doit()

    herobattlestage = HeroBattleStage(cur, wb)
    herobattlestage.doit()

    heroxuanyan = HeroXuanYan(cur, wb)
    heroxuanyan.doit()

    item = Item(cur, wb)
    item.doit()

    itemeffect = ItemEffect(cur, wb)
    itemeffect.doit()

    luckevent = LuckEvent(cur, wb)
    luckevent.doit()

    lucktip = LuckTip(cur, wb)
    lucktip.doit()

    lucktype = LuckType(cur, wb)
    lucktype.doit()

    lvparalimit = LvParaLimit(cur, wb)
    lvparalimit.doit()

    mission = Mission(cur, wb)
    mission.doit()

    person = Person(cur, wb)
    person.doit()

    province = Province(cur, wb)
    province.doit()

    resource = Resource(cur, wb)
    resource.doit()

    skill = Skill(cur, wb)
    skill.doit()

    syspara = SysPara(cur, wb)
    syspara.doit()

    technology = Technology(cur, wb)
    technology.doit()

    tipmessage = TipMessage(cur, wb)
    tipmessage.doit()

    cur.close()
    conn.close()
except mdb.Error, e:
    conn.rollback()
    print "Error: %d: %s" % (e.args[0], e.args[1])

wb.save('qixiong.xls')
