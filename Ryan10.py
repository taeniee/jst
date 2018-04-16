# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="Elotib3fd5gKWGF7PT89.aQ6PkJ1/rpwh56KrqEElwq.w3XJUNzb4thLZcn2UNHPVelcxVsWVgUndcMQ8YtiP2Q=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ElLr2mB4EVX9rE5GegL0.3Tr3b+973USzrMn3/ZhI4a.EXxunS32UOTTAe9Enc67tUzbPqyU0bwHh5Nm/Uqvpk0=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="ElgxMvqjo2h5f7AJhQub.9tPmkBy3xN3DJsd9GTANoW.6lEoBL1aqzdCpzE6hdqs8TneZLWRs3Cy2+YWIG3r1ws=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="El3nxwC9syORFabIdup3.2KYukWrsURBRIvGTVgy6GW.lbDWjP8arb31/T2k1olIllDIp5TYKYep7dWppmfRzlM=")
kc.loginResult()

kb = LINETCR.LINE()
kb.login(token="ElQ1Gbc6bemseayFefD0.XlPOaCcb3llbJv7yoF+9ya.p2f8nOokafQ7Q+ok3EmSlkVtZgPuq9bnVbIqh/JZTP0=")
kb.loginResult()

kd = LINETCR.LINE()
kd.login(token="ElYBqfulV1M6aPKwD9C9.Z5FOM+X3LdX9eCuSNeAYUq.c9d5TnUKVe8VZ7J69hVtlz1waaOdmvqQ6CWQf4SZYi4=")
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token="El0QplA1fmHjF8PZ8E94.zChTzM4vLoRx8l6+nFkx1a.ISbjbUK04fzLsdmsbbzHCoZpptNMuThwEJLp69cwB44=")
ke.loginResult()

kh = LINETCR.LINE()
kh.login(token="ElYjFh0tWzrGfnC2HmC8.ClAYz1BdwvU7xyaf+IfXYa.0AM0hRP7XV0L9+8NyRwd9uOCb3jxi6rmsfY6WAzSzi4=")
kh.loginResult()

kj = LINETCR.LINE()
kj.login(token="ElvNHxUriySpjn7d2Ysb.A7WJape8j8cSmszvOoyucW.vL7ALTV7+kw0rXAlzGgJh4SbYTexzNl62ayswq5QTKM=")
kj.loginResult()

kf = LINETCR.LINE()
kf.login(token="ElYwQzegRTcYRqsuuutc.shHnRucHCJGBQJoaTKYYJa.ilWgWpEs6ltmC1Uxo5aZKMhws9Gvynkadzy8UPFNT6w=")
kf.loginResult()

kg = LINETCR.LINE()
kg.login(token="ElVSm4uuisjCoUbr6gx4.UvXL1mVd7A5I8AnRweKI9a.UGPTpcD76nPrcdvumEvnN776YP6rCeMKIpEp4HHfG0k=")
kg.loginResult()

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""  ➰└ Commands Bots ┐➰
     =====[ ѕєℓfтвσт ]=====
             
🔐  Me
🔐  TL: └ Text ┐
🔐  Mid
🔐  Up
🔐  Creator
🔐  Anju  ~  Cancel pending invite 1 by 1
🔐  Copy└ @ ┐
🔐  Speed, Sp
🔐  Your name
🔐  List group
🔐  Qr on/off
🔐  Namelock on/off
🔐  Clock on/off
🔐  Change clock 
🔐  Cn:└ Your Name ┐
🔐  Cancelall └ Reject spam invite ┐
🔐  Cancelall1└ K1 Reject spam invite ┐
🔐  Message set:└Text┐
🔐  Comment set:  └Text┐
🔐  My message
🔐  My comment
🔐  Add confirm
🔐  Ginfo
🔐  Mid└ @ ┐ Tag
🔐  Banlist
🔐  Cek ban
🔐  Ban  ~  Share contact
🔐  Unban  ~  Share contact
🔐  Ban └ @ ┐  Tag
🔐  Unban └ @ ┐  Tag
🔐  Seeyou ~  KICK BLACKLIST USER
🔐  Gurl └ View Link Groups ┐
🔐  Say  └ Text ┐
🔐  Cancel
🔐  Gn:  └ Name ┐ 
🔐  Maaf└ @ ┐ Tag
🔐  Nk  └ @ ┐ Tag
🔐  BL└ @ ┐ Tag
🔐  Sorry  └ @ ┐ Tag
🔐  Fuck
🔐  Hemmm  ~  Cleanse this group
🔐  Mentions
🔐  Invite  └ Mid ┐
🔐  Absen/Respon
🔐  Set  ~  View your setting
🔐  Gift
🔐  Gift1
🔐  Gift2
🔐  Gift3
🔐  Masuk beb ~ All Kicker join
🔐  Husss ~ All Kicker leave
🔐  Kuy1 /2/3~  All kicker join one by one

  ➰└ Commands Set ┐➰
       
🔐  Auto Like : on/off
🔐  Contact : on/off
🔐  Auto join : on/off
🔐  Auto Cancel : 1 on/off
🔐  Auto Like : on/off
🔐  Auto leave : on/off
🔐  Share : on/off
🔐  Auto add : on/off
🔐  Comment : on/off
🔐  Protect : on/off
🔐  Protect qr : on/off
🔐  Welcome : on/off
	
          ===[ ѕєℓfтвσт ]===
      ➰Řýąñ§hąđøw₩ąřr!ør✔✔"""
KAC=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = kd.getProfile().mid
Fmid = ke.getProfile().mid
Gmid = kg.getProfile().mid
Hmid = kh.getProfile().mid
Jmid = kj.getProfile().mid
Imid = kf.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Imid]
admin=["u02aea92a3d7e44f587e7a91141e78b59","uded47707ff7bdeeb19466377fb31e2e0","uf53a4c29b6375e7ddd8d20fd82d6a73b","uda4c942b0452bab6eb89582dbc663a83","uc4ba6801c081dcb2c18d5ed839fffd60","ucf97e89bfc77943c7d11c52c9c46b2b9","u70b6b26756c3595bbb5d8005fe2171c8","u65c1ed666e1594ead7f0bebf35f297d4"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks for add Created by Řýąñ\n\n>>  https://line.me/ti/p/~withme_sw\n>>  https://line.me/ti/p/~withme_sw",
    "lang":"JP",
    "comment":"🔹Auto like by ☞ Řýąñ  􀜁􀅔􀜁􀅔Har Har􏿿 \n\n>>  https://line.me/ti/p/~withme_sw\n>>  https://line.me/ti/p/~withme_sw",
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":False,
    "Backup":True,
    "qr":False,
    "pname":{},
    "pro_name":{},    
    "welcome":False,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

setTime = {}
setTime = wait2["setTime"]
contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                else:
                    	G = ki.getGroup(op.param1)                                                                        
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                else:
                    	X = kk.getGroup(op.param1)                                                                        
                        kk.kickoutFromGroup(op.param1,[op.param2])                       
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                else:
                    	X = kc.getGroup(op.param1)                                                                        
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kb.updateGroup(X)
                else:
                    	X = kb.getGroup(op.param1)                                                                        
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ticket = kb.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = kb.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                else:
                    	X = kd.getGroup(op.param1)                                                                        
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                else:
                    	X = kf.getGroup(op.param1)                                                                        
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ticket = kf.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Fmid:
                    if op.param2 in Dmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kb.updateGroup(X)
                else:
                    	X = kb.getGroup(op.param1)                                                                        
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ticket = kb.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kb.updateGroup(X)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Gmid:
                    if op.param2 in Amid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kg.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                else:
                    	G = ki.getGroup(op.param1)                                                                        
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Hmid:
                    if op.param2 in Emid:
                        X = kb.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                else:
                    	X = kd.getGroup(op.param1)                                                                        
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        wait["blacklist"][op.param2] = False
        if op.type == 13:
                if op.param3 in Jmid:
                    if op.param2 in Emid:
                        X = kb.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                else:
                    	X = kd.getGroup(op.param1)                                                                        
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        wait["blacklist"][op.param2] = False

        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
                        fuck=random.choice(klist) 
                        G = fuck.getGroup(op.param1)
                        fuck.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e      
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    kpist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
                    puck=random.choice(kpist) 
                    G = puck.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    puck.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kb.getGroup(op.param1)
				    except:
					try:
                                            G = kd.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        kb.updateGroup(G)
                                    except:
                                        try:
                                            kd.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
#------------------------[Welcome]----------------------------
        if op.type == 17:
          if wait["welcome"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            cl.sendText(op.param1, "Selamat Datang Di Grup " + str(ginfo.name))
            cl.sendText(op.param1, "Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
            print "MEMBER HAS LEFT THE GROUP"
        if op.type == 15:
            if op.param2 in admin:
                return
            cl.sendText(op.param1, "Good Bye kaka akoohhh 😎😎")
            print "MEMBER HAS LEFT THE GROUP"
#-------------------------------------------------------------------- 
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    kpist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
                    puck=random.choice(kpist) 
                    G = puck.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    puck.updateGroup(G)
                    puck.kickoutFromGroup(op.param1,[op.param2])                    
                    G = puck.getGroup(op.param1)   
                    G.preventJoinByTicket = True
                    puck.updateGroup(G)
                 except Exception, e:
                           print e
         
        if op.type == 13:
            U = cl.getGroup(op.param1)
            I = U.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
                    puck=random.choice(klist)
                    G = puck.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        puck.cancelGroupInvitation(op.param1, gInviMids)

        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        gs = kc.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        cl.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
                       kicker=random.choice(klist)                       
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       cl.updateGroup(G)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(op.param1)
                       ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       G = cl.getGroup(op.param1)             
                       G.preventJoinByTicket = True
                       kicker.kickoutFromGroup(op.param1,[op.param2])                       
                       ky.leaveGroup(op.param1)
                       cl.updateGroup(G)
                   except Exception, e:
                            print e
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because there is no kick regulation or group,\n["+op.param1+"]\nof\n["+op.param2+"]\nI could not kick.\nAdd it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)                    
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin: 
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Succes")
                        ki.sendText(msg.to,"Secces")
                        kk.sendText(msg.to,"Succes")
                        kc.sendText(msg.to,"Succes")
               
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"🔹[NAME]:\n" + msg.contentMetadata["displayName"] + "\n🔹[MID]:\n" + msg.contentMetadata["mid"] + "\n🔹[STATUS]:\n" + contact.statusMessage + "\n🔹[PICTURE STATUS]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n🔹[CoverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"🔹[NAME]:\n" + msg.contentMetadata["displayName"] + "\n🔹[MID]:\n" + msg.contentMetadata["mid"] + "\n🔹[STATUS]:\n" + contact.statusMessage + "\n🔹[PICTURE STATUS]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n🔹[CoverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("R1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("R1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("R2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("R2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("R3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("R3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "R1 kick " in msg.text:
                midd = msg.text.replace("R1 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "R2 kick " in msg.text:
                midd = msg.text.replace("R2 kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "R1 invite " in msg.text:
                midd = msg.text.replace("R1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "R2 invite " in msg.text:
                midd = msg.text.replace("R2 invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
                        
            elif msg.text in ["All cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = kk.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kk.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kk.sendText(msg.to,"No one is inviting")
                        else:
                            kk.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")            
            elif "gurl" == msg.text:
                print cl.getGroup(msg.to)
                cl.sendMessage(msg)
            elif msg.text in ["Qr on","Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R1 ourl","R1 link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done ")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R2 ourl","R2 link on"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done ")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Qr off","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R1 curl","R1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["R2 curl","R2 link off"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done ")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"➰ NAME GROUP ➰\n" + str(ginfo.name) + "\n\n🔹 Group Id \n" + msg.to + "\n\n🔹Creator \n" + gCreator + "\n\n🔹Status profile \nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n~  Members :: " + str(len(ginfo.members)) + " Members\n~  Pending :: " + sinvitee + " People\n~  URL  :: " + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Gc" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                kb.sendText(msg.to,Dmid)
                kd.sendText(msg.to,Emid)
                ke.sendText(msg.to,Fmid)
                kf.sendText(msg.to,Imid)
                kg.sendText(msg.to,Gmid)
                kh.sendText(msg.to,Hmid)
                kj.sendText(msg.to,Jmid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "R1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "R2 mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "TL: " in msg.text:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Protect:on","Protect on"]:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Protection Enable On")
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Protect qr off"]:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Protection QR Off")
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Protect qr on"]:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Protection QR On")
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR On")
                    else:
                        cl.sendText(msg.to,"Already on")                     
            elif msg.text in ["Protect:off","Protect off"]:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Protection Disable Off")
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Disable Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif ("Cn: " in msg.text):
              if msg.toType == 2:
                profile = cl.getProfile()
                X = msg.text.replace("Cn: ","")
                profile.displayName = X
                cl.updateProfile(profile)
                cl.sendText(msg.to,"Name  ~  " + X + " Done")
              else:
                cl.sendText(msg.to,"Failed")

            elif ("1Cn " in msg.text):
              if msg.toType == 2:
                profile = ki.getProfile()
                X = msg.text.replace("1Cn ","")
                profile.displayName = X
                ki.updateProfile(profile)
                ki.sendText(msg.to,"name " + X + " done")
              else:
                ki.sendText(msg.to,"Failed")
            elif ("2Cn " in msg.text):
              if msg.toType == 2:
                profile = kk.getProfile()
                X = msg.text.replace("2Cn ","")
                profile.displayName = X
                kk.updateProfile(profile)
                kk.sendText(msg.to,"name " + X + " done")
              else:
                kk.sendText(msg.to,"Failed")
            elif ("3Cn " in msg.text):
              if msg.toType == 2:
                profile = kk.getProfile()
                X = msg.text.replace("3Cn ","")
                profile.displayName = X
                kc.updateProfile(profile)
                kc.sendText(msg.to,"name " + X + " done")
              else:
                kk.sendText(msg.to,"Failed")
            elif msg.text in ["Mc: "]:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif ("Auto cancel: " in msg.text):
                try:
                    strnum = msg.text.replace("Auto cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share:on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share:off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
                        
            elif msg.text in ["Set"]:
                md = " ➰「  SETTING  」➰\n    ===[ѕєℓfтвσт]===\n\n"
                if wait["contact"] == True: md+="🔹 Contact  →  on\n"
                else: md+="🔹 Contact  →  off\n"
                if wait["autoJoin"] == True: md+="🔹 Auto join  →  on\n"
                else: md +="🔹 Auto join  →  off\n"
                if wait["autoCancel"]["on"] == True: md+="🔹 Auto cancel  → "+ str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "🔹 Auto cancel  →  off\n"
                if wait["likeOn"] == True: md+="🔹 Auto Like  →  on\n"
                else: md+="🔹 Auto Like  →  off\n"
                if wait["leaveRoom"] == True: md+="🔹 Auto leave  →  on\n"
                else: md+="🔹 Auto leave  →  off\n"
                if wait["timeline"] == True: md+="🔹 Share  →  on\n"
                else: md+="🔹 Share  →  off\n"
                if wait["autoAdd"] == True: md+="🔹 Auto add  →  on\n"
                else: md+="🔹 Auto add  →  off\n"
                if wait["commentOn"] == True: md+="🔹 Comment  →  on\n"
                else: md+="🔹 Comment  →  off\n"
                if wait["Backup"] == True: md+="🔹 Auto Backup  →  on\n"
                else: md+="🔹 Auto Backup  →  off\n"
                if wait["qr"] == True: md+="🔹 Protect QR : on\n"
                else: md+="🔹 Protect QR  →  off\n"
                if wait["protectionOn"] == True: md+="🔹 Protection  →  on\n"
                else: md+="🔹 Protection  →  off\n"
                if wait["welcome"] == True: md+="🔹 Welcome  →  on\n"
                else: md+="🔹 Welcome  →  off\n" 
                cl.sendText(msg.to,md + "\n    ===[ ѕєℓfтвσт ]===\n➰Řýąñ§hąđøw₩ąřr!ør✔✔")
            elif msg.text in ["Group id","List group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[🔹]   %s  \n" % (cl.getGroup(i).name + " :::: " + str(len (cl.getGroup(i).members)))
                cl.sendText(msg.to, "==== [MY GROUPS] ====\n\n"+ h +"\n TOTAL GROUPS : " +str(len(gid)))
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Cancelall1"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"All invitations have been refused")
                else:
                    ki.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Cancelall2"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"All invitations have been refused")
                else:
                    kk.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Backup on","backup:on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Backup On")
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Backup off","backup:off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Backup Off")
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Auto like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Auto like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "My message" in msg.text:
                cl.sendText(msg.to,"Your message ⤵\n\n" + str(wait["message"]))
            elif "Message set: " in msg.text:
                m = msg.text.replace("Message set: ","")
                if m in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["message"] = m
                    cl.sendText(msg.to,"Changed ⤵\n\n" + m)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Changed ⤵\n\n" + c)
            elif msg.text in ["Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment:off","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚") 
            elif msg.text in ["Welcome on"]:
                if wait["welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Welcome off"]:
                if wait["welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["My comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"Your comment ⤵\n\n" + str(wait["comment"]))
            elif msg.text in ["Creator"]:
            	msg.contentType = 13
                msg.contentMetadata = {'mid': 'u02aea92a3d7e44f587e7a91141e78b59'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "My creator ⤴")
                random.choice(KIL).sendText(msg.to, "My creator ⤴")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["2gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "[]" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clock on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Clock off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,".")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock.")
        
#-----------------------------------------------
            elif msg.text == "Check":
                    cl.sendText(msg.to, "Check in a readPoint")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    
            elif msg.text == "Lurk on":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------
            elif "Maaf " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Maaf ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:                                    
                                    G = cl.getGroup(msg.to)
                                    ginfo = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    time.sleep(0.2)
                                    G = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = True
                                    kc.kickoutFromGroup(msg.to,[target])
                                    kc.leaveGroup(msg.to)
                                    cl.updateGroup(G)
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes ")
                                    kk.sendText(msg.to,"Bye")
            elif "Sorry " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Maaf ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:                                    
                                    G = cl.getGroup(msg.to)
                                    ginfo = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    time.sleep(0.2)
                                    G = cl.getGroup(msg.to)
                                    G.preventJoinByTicket = True
                                    kk.kickoutFromGroup(msg.to,[target])
                                    kk.leaveGroup(msg.to)
                                    cl.updateGroup(G)
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes ")
                                    kk.sendText(msg.to,"Bye")

#-----------------------------------------------                   
            elif msg.text in ["Masuk beb"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        kk.updateGroup(G)

            elif msg.text in ["Kuy1"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Kuy2"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Kuy3"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            
#-----------------------------------------------
            elif msg.text in ["Husss"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kf.leaveGroup(msg.to)
                        kg.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye1"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye2"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Lc @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Hy @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:     
                        pass
#------------------------[Copy]-------------------------
            elif msg.text in ["Backup"]:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to,"Backup done")
                    except Exception as e:
                        cl.sendText(msg.to, str (e))
                        
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[Copy]"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found")
                    else:                                                                                                                       
                        for target in targets:
                            try:
                                cl.CloneContactProfile(target)
                                cl.sendText(msg.to, "Succes")
                            except Exception as e:
                                print e
#-----------------------------------------------
            elif msg.text in ["Fuck"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Bye")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Hemmm" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Hemmm","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    ki.sendText(msg.to,"Just some casual cleansing ")
                    kk.sendText(msg.to,"Group cleansed.")
                    kk.sendText(msg.to,"Bye All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                kk.sendText(msg,to,"Group cleanse")
             
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:                               
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes ")
                                    kk.sendText(msg.to,"Bye")
            elif "BL @" in msg.text:
                _name = msg.text.replace("BL @","")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes ")
                                except:
                                    cl.sendText(msg.to,"error")
            elif "Ban " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:                                        
                       ban0 = msg.text.replace("Ban ","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Success")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Success")
                                
            elif "Mentions" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//300
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
                                
            elif "Unban " in msg.text:
               if msg.toType == 2:
                  if msg.from_ in admin:                                        
                       unb0 = msg.text.replace("Unban ","")
                       unb1 = unb0.lstrip()
                       unb2 = unb1.replace("@","")
                       unb3 = unb2.rstrip()
                       x_name = unb3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if x_name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Success")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Success")

            elif "Namelock on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Turned on")
                else:
                    cl.sendText(msg.to,"Already on")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Turn off")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"Already off")
            
            elif "Mid " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Your mid ⤵\n" + contact.mid)
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + str(cu))

            elif "Kick " in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass

#-----------------------------------------------
            elif msg.text in ["Tes"]:
                klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh,kj]
                N=random.choice(klist)
                N.sendText(msg.to,"I am Ready 😎")
#-----------------------------------------------
            elif "Say " in msg.text:
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    kb.sendText(msg.to," " + string + " ")
                    kd.sendText(msg.to," " + string + " ")
                    ke.sendText(msg.to," " + string + " ")
                    kf.sendText(msg.to," " + string + " ")
                    kg.sendText(msg.to," " + string + " ")
                    kh.sendText(msg.to," " + string + " ")
                    kj.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
#-----------------------------------------------
            elif msg.text in ["Absen","Respon"]:              
                ki.sendText(msg.to,"Kicker 1 Hadiirrr")
                kk.sendText(msg.to,"Kicker 2 Hadirr")
                kc.sendText(msg.to,"Kicker 3 Hadirr")
                kb.sendText(msg.to,"Kicker 4 Hadiirrr")
                kd.sendText(msg.to,"Kicker 5 Hadirr")
                ke.sendText(msg.to,"Kicker 6 Hadirr")
                kg.sendText(msg.to,"Kicker 7 Hadiirrr")
                kh.sendText(msg.to,"Kicker 8 Hadirr")
                kj.sendText(msg.to,"Kicker 9 Hadirr")
                kf.sendText(msg.to,"Kicker 10 Hadiirrr")
                kf.sendText(msg.to,"======[ DONE BOS ]======")

#-----------------------------------------------
            elif msg.text in ["Your name","your name"]:
                G = ki.getProfile()
                X = G.displayName
                Y = kk.getProfile()
                Z = Y.displayName
                A = kc.getProfile()
                B = A.displayName
                ki.sendText(msg.to,X)
                kk.sendText(msg.to,Z)
                kc.sensText(msg.to,B)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))


#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                    ki.sendText(msg.to,"nothing")
                    kk.sendText(msg.to,"nothing")
                    kc.sendText(msg.to,"nothing")

                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "~ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    ki.sendText(msg.to,mc)
                    kk.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Seeyou"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"There was no blacklist user")
                        kk.sendText(msg.to,"There was no blacklist user")
                        kc.sendText(msg.to,"There was no blacklist user")
                        
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])                        
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user")
                    ki.sendText(msg.to,"Blacklist user")
                    kk.sendText(msg.to,"Blacklist user")
                    
            elif msg.text in ["Anju"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"😨😨😨😨😨")

        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass


        if op.type == 59:
            print op


    except Exception as error:
        print error

def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kb.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kd.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ke.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kf.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kg.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kh.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(500)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
