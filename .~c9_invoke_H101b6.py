# -*- coding: utf-8 -*-

import JST
from JST.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,ast,re,os,string,requests,subprocess,ctypes,tempfile,glob,shutil,unicodedata,urllib,urllib2

cl = JST.LINE()
cl.login(token="EnEK6x4IKxl1bniGrdh9.e+k3F53WXfjVspleffqcwq.Zr6t5LzBWAwjNPeax5PPYWz64jNVhX/LhmxoSPLsAMM=")
cl.loginResult()

ki = JST.LINE()
ki.login(token="EmWO8e4UY0USqkaBbzU0.CgZqbGyU9jtFjlzYVY0aya.tFhA2SfPfNEePxna8g8X4I16EY7ygGQ6Z+57X3UHgA0=")
ki.loginResult()

ki2 = JST.LINE()
ki2.login(token="EnRwpi3mZNw2ixw5mGl0.dgOEPTvqhsVLUYDLD5n04a.U6lVPN+eFBHMpMMOFMxXy/9Tlu5SmlZ5mVFlWTnKres=")
ki2.loginResult()

ki3 = JST.LINE()
ki3.login(token="Emx2EInqHaLL6eZeRSKa.ZtkpH+DhRtV3BYJ71fmmEG.emeB4qNxhy/V/96RX7CdGuAzhWVDrOX7jH6TCoLRRWI=")
ki3.loginResult()

ki4 = JST.LINE()
ki4.login(token="EmagkCFTE8Jz4sNjy6Vb.hiAf2SzXRil+UQyDCaF/kW.EmpVBcv9TcUyk23hQ5SEiKeN5W76227x7vNTuwI2bk8=")
ki4.loginResult()

ki5 = JST.LINE()
ki5.login(token="Em3SlXnmEsbbXsaqq5G5.psGqLYm9+MM53POk1HTynq.WHyrAAKoDvOpEtldX5AElVvmwbOaOBRxO+HfYYENak8=")
ki5.loginResult()

ki6 = JST.LINE()
ki6.login(token="EmdhMG8djOWrMDlRdNPf.yb/UJa2vwZus1dMVvrghxW.lkTTEao/M6Jj30zOZF2j5kXuYEgXeOLR8EGHQYJUkQs=")
ki6.loginResult()

ki7 = JST.LINE()
ki7.login(token="Emj7XSzfxluRAdFOVOW1.drzwL75km/oml8p8e6KgOq.YFQoyJrIG0PaAGx0/FEfZpMVp3hnFn4jwY+wR9+U2Yw=")
ki7.loginResult()

print "succes geb"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""┏━━━━ೋ• ❄ •ೋ━━━━┓
☬   ❁          ᴊ̈̋̊ͦs̍ͫ̓̚ᴛ͗̊̆ͪ'͂͐̉ͣᴛͮ̃̊͌ ᴅ͇̠̣̤ᴇ͊̉̐ͯғ̿̍ͨ̈ᴇͥ͛̏̄ɴ̣̯̹͌ᴅͤͧͧ̈́ᴇ̌̐ͬ͌ʀͮ̽͋ͤ           ❁   ☬
┗━━━━ೋ• ❄ •ೋ━━━━┛

           => ᴴᴱᴿᴱ ᴵˢ ᵀᴴᴱ ᶜᴼᴹᴹᴬᴺᴰ <=

❂͜͡☆➣ [Id] 
❂͜͡☆➣ [Mid] 
❂͜͡☆➣ [Mc @]
❂͜͡☆➣ [Mc:] 
❂͜͡☆➣ [Me] 
❂͜͡☆➣ [TL: 「Text」]
❂͜͡☆➣ [MyName:]
❂͜͡☆➣ [Gift] 
❂͜͡☆➣ [Mid 「mid」 ]
❂͜͡☆➣ [Searchid:] 
❂͜͡☆➣ [Glist] 
❂͜͡☆➣ [Group id] 
❂͜͡☆➣ [Gcreator] 
❂͜͡☆➣ [Creator] 
❂͜͡☆➣ [album 「id」] 
❂͜͡☆➣ [Hapus album 「id」]
❂͜͡☆➣ [Gcancel] 
❂͜͡☆➣ [Gbc「Group」]
❂͜͡☆➣ [Bc:「Contact」]
❂͜͡☆➣ [Myname]
❂͜͡☆➣ [Mybio]
❂͜͡☆➣ [Mypict]
❂͜͡☆➣ [Mycover]
❂͜͡☆➣ [Ban「Send contact」]
❂͜͡☆➣ [Unban「Send contact」]
❂͜͡☆➣ [Banlist] 
❂͜͡☆➣ [Com on] 
❂͜͡☆➣ [Com off] 
❂͜͡☆➣ [Com set] 
❂͜͡☆➣ [Mcheck]
❂͜͡☆➣ [Message Confirmation] 
❂͜͡☆➣ [Mybio: 「Isi Bio」] 
❂͜͡☆➣ [Allbio: 「Isi Bio bot」]
❂͜͡☆➣ [Steal pict 「@」]
❂͜͡☆➣ [Steal cover 「@」]
❂͜͡☆➣ [Steal bio 「@」]
❂͜͡☆➣ [Steal name 「@」]
❂͜͡☆➣ [Cium] 
❂͜͡☆➣ [Cipok「Group 150-500mem」] 
❂͜͡☆➣ [Cctv] 
❂͜͡☆➣ [Cipok「Group 150-500mem」] 
❂͜͡☆➣ [Invite「Send contact」] 
❂͜͡☆➣ [Invite「mid」] 
❂͜͡☆➣ [Kmid: Kick by mid] 
❂͜͡☆➣ [Ginfo] 
❂͜͡☆➣ [Glist] 
❂͜͡☆➣ [Cancel] 
❂͜͡☆➣ [Backup] 
❂͜͡☆➣ [Gn 「Nama grup」 
❂͜͡☆➣ [Gurl] 
❂͜͡☆➣ [gurl「kelompok ID」
❂͜͡☆➣ [Kick「@」] 
❂͜͡☆➣ [NK:] 
❂͜͡☆➣ [Sory 「@」] 
❂͜͡☆➣ [BTS in] 
❂͜͡☆➣ [BTS out] 
❂͜͡☆➣ [Member?]
❂͜͡☆➣ [Mayhem]
❂͜͡☆➣ [Sett]
❂͜͡☆➣ [「name」in]
❂͜͡☆➣ [Bye「name」]
❂͜͡☆➣ [Bye me]
❂͜͡☆➣ [Respon]
❂͜͡☆➣ [Papay]
❂͜͡☆➣ [Kam]
❂͜͡☆➣ [Lyric「songname」]
❂͜͡☆➣ [Wiki「title」]
❂͜͡☆➣ [Instagram「name」]
❂͜͡☆➣ [Music「songname」]
❂͜͡☆➣ [Youtube「videoname」]
❂͜͡☆➣ [Video「video on yt」]
❂͜͡☆➣ [BotStikers{Hore,Lol,No,Ok}] 

★ ℳîℳîℂ ★

❂͜͡☆➣ [Mimic on/off]
❂͜͡☆➣ [Target「@」]
❂͜͡☆➣ [Del target「@」]
❂͜͡☆➣ [Targetlist]
❂͜͡☆➣ [Mimic set to「me/target」]

☬ S⃟e⃟t ☬

❂͜͡☆➣ [Link on/off]
❂͜͡☆➣ [Contact on/off] 
❂͜͡☆➣ [Auto join on/off] 
❂͜͡☆➣ [Auto leave on/off] 
❂͜͡☆➣ [Auto add on/off] 
❂͜͡☆➣ [Jam on/off]
❂͜͡☆➣ [Mention on/off]
❂͜͡☆➣ [Like on/off]
❂͜͡☆➣ [Backup on/off]
❂͜͡☆➣ [Protect on/off]
❂͜͡☆➣ [qrprotect on/off]
❂͜͡☆➣ [Inviteprotect on/off]
❂͜͡☆➣ [Cancelprotect on/off]
❂͜͡☆➣ [Allprotect on/off]
❂͜͡☆➣ [Mem pro on/off]
=============================

            ┏━ೋ• ❄ •ೋ━━━━━┓
Support by : ☬ ᴛᴇᴀᴍ ᴊᴏᴋᴇʀ ʙᴏᴛs ☬
                  ┗━━━━━ೋ• ❄ •ೋ━┛

"""
helo=""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7]
DEF=[ki,ki2,ki3,ki4,ki5,ki6,ki7]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,"u13f2b77f9df0c4526f48f2c414540259"]
admin = ["u13f2b77f9df0c4526f48f2c414540259"]
staff = ["u13f2b77f9df0c4526f48f2c414540259"]
adminMID = "u13f2b77f9df0c4526f48f2c414540259"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':" Knp add Cogan??",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "likeOn":False,
    "commentOn":True,
    "commentBlack":{},
    "detectMention": True,
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Backup":True,
    "protect":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
    "MProtection":False,
    "ProtectQR":True,
    "Allprotect":False,
}


def cms(string, commands): #/XXX, &gt;XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/","&gt;",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']


contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
#-----------------------------------------------#
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
    try:
        cl.sendText(op.param1, cl.getContact(op.param2).displayName + "Selamat Datang😊\n " + group.name + "Salam Kenal Kak")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param3).displayName + " Jangan Main Kick!\n(/*´･ω･*\)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

def NOTIFIED_LEAVE_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param2).displayName + " Papay\n(*´･ω･*)")
        ki.sendText(msg,to,"Semoga Tenang Bagi yang Meninggalkan Grup 🏳️")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return
#-----------------------------------------------
def bot(op):
    try:
        if op.type == 0:
            return
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

        #if op.type == 15:
     #       random.choice(DEF).sendText(op.param1, "yg tenang di Alam Sana :)")
       #     print op.param3 + "has left the group"

        #if op.type == 17:
            #group = ki2.getGroup(op.param1)
            #cb = Message()
            #cb.to = op.param1
            #cb.text = ki2.getContact(op.param2).displayName + " Selamat Datang di " + group.name
            #ki2.sendMessage(cb)
            
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・" + Name + "\n " + datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・" + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass

        if op.type == 25:
            msg = op.message
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg.from_ in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg.from_]
                        else:
                            pass
                    except:
                        pass
                else:
                    pass

            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as error:
                print error
                print ("\n\nRECEIVE_MESSAGE\n\n")
                return         
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if 'MENTION' in msg.contentMetadata.keys() != None:
              if wait ["detectMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["tαg = ϼϵͷs",cName + " kαͷgϵͷ ϒαh.....",cName + " Penting pc aja","ᴅᴏɴᴛ ᴛᴀɢ ᴍᴇ, ᴅᴀsᴀʀ ғᴀɴs "]
                    ret_ = " " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                if wait["akaInvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddyhh to use command !, \n➡ Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"✍⎯Cogan__Ȿ⟿ℬᝪᝨ⟿☬ Invited: \n➡ " + _name)
                                     wait["akaInvite"] = False
                                     break
                                 except:
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait["akaInvite"] = False
                                          break
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.text in ["Backup","backup"]:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to,"Backup done")
                    except Exception as e:
                        cl.sendText(msg.to, str (e))
            elif "Copy @" in msg.text:
               if msg.toType == 2:
                   print"[Copy]"
                   _name = msg.text.replace("Copy @","")
                   _nametarget = _name.rstrip(' ')
                   gs = cl.getGroup(msg.to)
                   targets=[]
                   for g in gs.members:
                       if _nametarget == g.displayName:
                          targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to,"Not Found")
                   else:
                       for target in targets:
                           try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to,"Success Copy")
                           except Exception as e:
                               print e 

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif "Gn:" in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif "Gn " in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif msg.text.lower() == 'invite':
                if msg.from_ in admin:
                  if msg.toType == 2:
                    wait["akaInvite"] = True
                    ki.sendText(msg.to,"send contact 😉")
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Member?" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "S1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "S2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "S3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "S4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "S5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "S6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "S7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif msg.text.lower() == 'hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'siap bos':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'tanks':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846759",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'lol':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846776",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'sue':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'no':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'suntuk':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875040",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'apa':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == '?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'pose dulu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875030",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == '250c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1380280'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == '200c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1319678'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'njiir':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1300191'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'hadiah':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '5033'}
                msg.text = None
                cl.sendMessage(msg)

                ki6.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Gift you","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)     
            elif msg.text in ["BCancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Batal"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
                                               
            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"It was changed。\n\n" + c)
            elif msg.text in ["Comment check"]:
                 cl.sendText(msg.to,"An automatic comment is established as follows at present。\n\n" + str(wait["comment"]))
            elif msg.text in ["コメント:オン","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["コメント:オフ","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")                        
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close ô€¨👈")
                    else:
                        cl.sendText(msg.to,"URL close ô€¨👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
                        
            elif "Tiket " in msg.text.lower():
                rplace=msg.text.lower().replace("Tiket ")
                if rplace == "on":
                        wait["atjointicket"]=True
                elif rplace == "off":
                        wait["atjointicket"]=False
                cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                        if l not in n_links:
                                n_links.append(l)
                for ticket_id in n_links:
                        if wait["atjointicket"] == True:
                                group=cl.findGroupByTicket(ticket_id)
                                cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))  

            elif msg.text.lower() == "Invite:gcreator":
                if msg.toType == 2:
                       ginfo = cl.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           cl.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           cl.inviteIntoGroup(msg.to,[gcmid])
            elif msg.text.lower() == 'bot:gcreator':
                if msg.toType == 2:
                       ginfo = ki.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           ki.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           ki.inviteIntoGroup(msg.to,[gcmid])

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
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}                          
                cl.sendText(msg.to,"「 ID 」\nGroup Name:\n" + str(ginfo.name) + "\n\nGroup ID:\n" + msg.to + "\n\nGroup Creator:\n" + gCreator + "\n\nProfile status:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nmembers:" + str(len(ginfo.members)) + " members\npending:" + sinvitee + " people\nURL:" + u + "it is inside")
                cl.sendMessage(msg)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Gcreator" == msg.text:
              if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator)
            elif msg.text in ["Creator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    Creatorbot = "u13f2b77f9df0c4526f48f2c414540259"
                    try:
                        msg.contentMetadata = {'mid': Creatorbot}
                        
                    except:
                        Creatorbot = "Error"
                    cl.sendText(msg.to, "Created By")
                    cl.sendMessage(msg)

            elif msg.text.lower() == "Glist":
                gs = cl.getGroupIdsJoined()
                num=1
                L = "   ☫『 Groups-⚚-List 』☫\n"
                for i in gs:
                    L += "\n%i. %s\n%s\n" % (num, cl.getGroup(i).name + " | " + str(len (cl.getGroup(i).members)), i)
                    num=(num+1)
                L += "\n\n☫ Total Groups : [ %i ]" % len(gs)
                cl.sendText(msg.to, L + "\n\n                   °✍☬⟿BTS TEAM⟿☬̢ ") 
            elif msg.text in ["List group"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[~]%s\n" % (cl.getGroup(i).name   +str (len (cl.getGroup(i).members)))
                    cl.sendText(msg.to,"========[My Group]========\n"+ h +"Total Group :" +str(len(gid)))
            elif "Memid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
            elif "Bab" in msg.text:
                ki.sendText(msg.to,"☬⟿ℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki2.sendText(msg.to,"☬⟿ℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki3.sendText(msg.to,"☬⟿ℬᝪᝨ⟿☬ Ready 􀜁boss!!!")
                ki4.sendText(msg.to,"☬⟿ℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki5.sendText(msg.to,"☬⟿ℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki6.sendText(msg.to,"☬⟿ℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki7.sendText(msg.to,"☬⟿ℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
            elif "TL: " in msg.text:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&amp;postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "👈")
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#---------------------------------------------------------
            elif "S1name:" in msg.text:
                string = msg.text.replace("S1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S2name:" in msg.text:
                string = msg.text.replace("S2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S3name:" in msg.text:
                string = msg.text.replace("S3name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S4name:" in msg.text:
                string = msg.text.replace("S4name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S5name:" in msg.text:
                string = msg.text.replace("S5name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S6name:" in msg.text:
                string = msg.text.replace("S6name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S7name:" in msg.text:
                string = msg.text.replace("S7name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
#========================================
            elif msg.text in ["Myname"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[Name]===\n" + h.displayName)
#========================================
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[Status]===\n" + h.statusMessage)
#========================================
#===============Image====================#
            elif msg.text in ["Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
#==============Image finish================#
#========================================
            elif 'Lyric ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('Lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif 'Wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("Wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif 'Instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("Instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'Music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('Music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            elif "Youtube " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Video ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Video ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")
#========================================
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protectall on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["calncelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁??􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁����􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah On ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈") 
            elif msg.text in ["Protectall off","Proall off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Protect off","Pro off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Qrprotect off","Qr off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Inviteprotect off","Invite off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰����")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Cancelprotect off","Cancel off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Auto leave on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Auto leave off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","K on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","K off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif msg.text.lower() == 'Sett':
                md = "✃┈┈☫🛡 รεƭƭเɳɠร 🛡 ☫┈┈✍ \n\n"
                if wait["contact"] == True: md+=" ❂͜͡☆➣ Contact: ✔ \n"
                else: md+=" ❂͜͡☆➣Contact: ❌ \n"
                if wait["autoJoin"] == True: md+=" ❂͜͡☆➣ Auto Join: ✔ \n"
                else: md +=" ❂͜͡☆➣ Auto Join: ❌ \n"
                if wait["autoCancel"]["on"] == True: md+=" ❂͜͡☆➣ Auto cancel:" + str(wait["autoCancel"]["members"]) + " \n"
                else: md+=" ❂͜͡☆➣ Group cancel: ❌ \n"
                if wait["likeOn"] == True: md+=" ❂͜͡☆➣ Auto Like: ✔ \n"
                else: md+=" ❂͜͡☆➣ Auto Like: ❌ \n"
                if wait["detectMention"] == True: md+=" ❂͜͡☆➣ Auto respon: ✔ \n"
                else: md+=" ❂͜͡☆➣ Auto respond: ❌ \n"
                if wait["leaveRoom"] == True: md+=" ❂͜͡☆➣ Auto leave: ✔ \n"
                else: md+=" ❂͜͡☆➣ Auto leave: ❌ \n"
                if wait["timeline"] == True: md+=" ❂͜͡☆➣ Share: ✔ \n"
                else:md+=" ❂͜͡☆➣ Share: ❌ \n"
                if wait["autoAdd"] == True: md+=" ❂͜͡☆➣ Auto add: ✔ \n"
                else:md+=" ❂͜͡☆➣ Auto add: ❌ \n"
                if wait["Backup"] == True: md+=" ❂͜͡☆➣ Backup: ✔ \n"
                else:md+=" ❂͜͡☆➣ Backup: ❌ \n"
                if wait3["copy"] == True: md+=" ❂͜͡☆➣ Mimic: ✔ \n"
                else:md+=" ❂͜͡☆➣ Mimic: ❌ \n"
                if wait["commentOn"] == True: md+=" ❂͜͡☆➣ Auto Coment: ✔ \n"
                else:md+=" ❂͜͡☆➣ Auto Coment: ❌ \n"
                if wait["protect"] == True: md+=" ❂͜͡☆➣ Protect: ✔ \n"
                else:md+=" ❂͜͡☆➣Protect: ❌ \n"
                if wait["linkprotect"] == True: md+=" ❂͜͡☆➣ ProtectQr: ✔ \n"
                else:md+=" ❂͜͡☆➣ PotectQr: ❌ \n"
                if wait["inviteprotect"] == True: md+=" ❂͜͡☆➣ Invite Protect: ✔ \n"
                else:md+=" ❂͜͡☆➣ Invite Protect: ❌ \n"
                if wait["MProtection"] == True: md+=" ❂͜͡☆➣ MProtection: ✔ \n"
                else: md+=" ❂͜͡☆➣ MProtection: ❌ \n"
                if wait["cancelprotect"] == True: md+=" ❂͜͡☆➣ Cancel Protect: ✔ \n"
                else:md+=" ❂͜͡☆➣ Cancel Protect: ❌ \n"
                if wait["atjointicket"] == True: md+=" ❂͜͡☆➣ AtJoin Group Ticket: ✔ \n"
                else:md+=" ❂͜͡☆➣ Atjoin Group Ticket: ❌ \n\n ☬⟿ℛℹℴ⟿Ȿ⟿ℬᝪᝨ⟿☬"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Mee"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊upupupup")            
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album " in msg.text:
                gid = msg.text.replace("Album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text.lower() == 'BTSoutAllGroup':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to," Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Group cancelall","Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["MProtection:on","Mem pro on"]:
                if wait["MProtection"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                   wait["MProtection"] = True
                   if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection On")
                   else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["MProtection:off","Mem pro off"]:
                if wait["MProtection"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                   wait["MProtection"] = False
                   if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection Off")
                   else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Backup:on","Backup on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Backup On")
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Backup:off","Backup off"]:
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
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Like:off","Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Auto add on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add:" in msg.text:
                wait["message"] = msg.text.replace("Pesan add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Com Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Comen","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“??")
            
            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Bladd"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Bldel"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")

            elif msg.text in ["Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    kontak = cl.getContacts(commentBlack)
                num=1
                msgs="User Blacklist List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blacklist user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) < 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'up':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif 'crash' in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Mid_Here,'"}
                cl.sendMessage(msg)

            elif msg.text == "Cctv":
            	 if msg.toType == 2:
                    cl.sendText(msg.to, "Cctv mode On..")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait
            elif msg.text == "Liat":
            	 if msg.toType == 2:
                    print "Sider check aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "✍⎯ℓιѕт-⚚-тєя¢у∂υк̡͏̧⎯☫\n %s\n\n✍⎯кαηg-⚚-ιηтιρєяѕ⎯☫\n \n%s\n==========================\nIn the last seen point:\n[%s]\n==========================\n✍⎯by_☬⟿Cogan⟿☬_"% (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait                                                                                               
                        #cl.sendText(msg.to, "== Bakekok Sider == %s\nthat's it\n\nPeople who have ignored reads\n%skampret lo sider. ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「Cctv」you can send ♪ read point will be created ♪")      
#-----------------------------------------------
#VIEWSEEN TARO DISINI
#-----------------------------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed from the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Add admin @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]admin add executing"
                    _name = msg.text.replace("Add admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove admin @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]admin remove executing"
                    _name = msg.text.replace("Remove admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed from the admin list")
                            except:
                                pass
                    print "[Command]admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
            
            elif msg.text in ["Adminlist","adminlist"]:
                if admin == []:
                    ki.sendText(msg.to,"The Admin list is empty")
                else:
                    ki.sendText(msg.to,"Admin list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"

#========================================
            elif "Steal bio @" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
#========================================
#========================================
            elif "Steal name @" in msg.text:
                _name = msg.text.replace("Steal name @","")
                _nametarget = _name.rstrip(" ")
                gs = cl.getGroup(msg.to)
                for h in gs.members:
                    if _nametarget == h.displayName:
                       cl.sendText(msg.to,"[Name]:\n" + h.displayName )
                    else:
                         pass
#========================================
                    
            #elif msg.text in ["Ip Like", "Ar like"]:
                #if msg.from_ in staff:
                    #print "[Command]Like executed"
                    #cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    #try:
                        #likePost()
                    #except:
                        #pass
#batas__________________

            #elif "staff add @" in msg.text:
                #if msg.from_ in admin:
                    #print "[Command]Staff add executing"
                    #_name = msg.text.replace("Ar staff add @","")
                    #_nametarget = _name.rstrip('  ')
                    #gs = ki.getGroup(msg.to)
                    #gs = ki3.getGroup(msg.to)
                    #gs = ki4.getGroup(msg.to)
                    #gs = ki5.getGroup(msg.to)
                    #gs = ki6.getGroup(msg.to)
                    #targets = []
                    #for g in gs.members:
                        #if _nametarget == g.displayName:
                            #targets.append(g.mid)
                    #if targets == []:
                     #   ki.sendText(msg.to,"Contact not found")
                    #else:
                     #   for target in targets:
                      #      try:
                       #         staff.append(target)
                        #        cl.sendText(msg.to,"Added to the staff list")
                         #   except:
#                                pass
 #                   print "[Command]Staff add executed"
   #             else:
   #                 cl.sendText(msg.to,"Command denied.")
   #                 cl.sendText(msg.to,"Admin permission required.")
#------------------tes coba staf----------bawah
    #        elif "Staff add @" in msg.text:
     #           if msg.from_ in admin:
      #              print "[Command]Staff add executing"
       #             _name = msg.text.replace("Staff add @","")
        #            _nametarget = _name.rstrip('  ')
         #           gs = cl.getGroup(msg.to)
          #          gs = ki.getGroup(msg.to)
          #          gs = ki1.getGroup(msg.to)
           #         gs = ki2.getGroup(msg.to)
            #        gs = ki3.getGroup(msg.to)
             #       gs = ki4.getGroup(msg.to)
              #      gs = ki6.getGroup(msg.to)
               #     targets = []
                #    for g in gs.members:
                 #       if _nametarget == g.displayName:
                  #          targets.append(g.mid)
                   # if targets == []:
#                        ki.sendText(msg.to,"Contact not found")
 #                   else:
  #                      for target in targets:
   #                         try:
    #                            staff.append(target)
     #                           cl.sendText(msg.to,"Added to the staff list")
      #                      except:
       #                         pass
        #            print "[Command]Staff add executed"
         #       else:
         #           cl.sendText(msg.to,"Command denied.")
 #                   cl.sendText(msg.to,"Admin permission required.")
#
  #          elif "staff remove @" in msg.text:
   #             if msg.from_ in admin:
    #                print "[Command]Staff remove executing"
     #               _name = msg.text.replace("staff remove @","")
      #              _nametarget = _name.rstrip('  ')
       #             gs = cl.getGroup(msg.to)
        #            gs = ki.getGroup(msg.to)
         #           gs = ki1.getGroup(msg.to)
          #          gs = ki2.getGroup(msg.to)
           #         gs = ki3.getGroup(msg.to)
            #        gs = ki4.getGroup(msg.to)
             #       gs = ki5.getGroup(msg.to)
              #      gs = ki6.getGroup(msg.to)
               #     targets = []
                #    for g in gs.members:
                  #      if _nametarget == g.displayName:
                 #           targets.append(g.mid)
                   # if targets == []:
                    #    ki.sendText(msg.to,"Contact not found")
                    #else:
                     #   for target in targets:
                      #      try:
               #                 staff.remove(target)
              #                  cl.sendText(msg.to,"Removed to the staff list")
             #               except:
            #                    pass
           #         print "[Command]Staff remove executed"
          #      else:
         #           cl.sendText(msg.to,"Command denied.")
        #            cl.sendText(msg.to,"Admin permission required.")

#            elif msg.text in ["Stafflist","stafflist"]:
 #               if staff == []:
  #                  cl.sendText(msg.to,"The stafflist is empty")
   #             else:
    #                cl.sendText(msg.to,"Staff list:")
     #               mc = ""
       #             for mi_d in staff:
      #                  mc += "->" +cl.getContact(mi_d).displayName + "\n"
         #           cl.sendText(msg.to,mc)
        #            print "[Command]Stafflist executed"

#----------------------------------------------- atas 
            elif "Sory " in msg.text:
                if msg.toType == 2:
                  if msg.from_ in admin:
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                         targets.append(x["M"])
                     for target in targets:
                        try:
                           klist=[ki,ki1,ki2,ki3,ki4,ki5,ki6,ki7]
                           kicker = random.choice(klist)
                           if msg.from_ not in target:
                             kicker.kickoutFromGroup(msg.to,[target])
                             print (msg.to,[g.mid])
                        except:
                             ki.sendText(msg.to,"ops... \nSorry.... \ Aim khilaf......")
            elif "Say " in msg.text:
                       nk0 = msg.text.replace("Say ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
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
                                    ki7.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki7.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Kick " in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                           ki2.kickoutFromGroup(msg.to,[target])
                           ki3.kickoutFromGroup(msg.to,[target])
                           ki4.kickoutFromGroup(msg.to,[target])
                           ki5.kickoutFromGroup(msg.to,[target])
                           ki6.kickoutFromGroup(msg.to,[target])
                           ki7.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif "Cek " in msg.text:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Beb " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
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
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------

#-----------------------------------------------------------
	    elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Locked")
                            except:
                                cl.sendText(msg.to,"Success band...")
	    elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Success unband..")
            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
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
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Success band")
            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
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
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Success unband..")
#-----------------------------------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"ٴℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki2.sendText(msg.to,"ٴℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki3.sendText(msg.to,"ٴℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki4.sendText(msg.to,"ٴℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki5.sendText(msg.to,"ٴℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki6.sendText(msg.to,"ٴℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
                ki7.sendText(msg.to,"ٴℬᝪᝨ⟿☬ Ready 􀜁􀆴boss!!!")
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif msg.text in ["Respon"]:
                S1 = ki.getProfile()
                S2 = ki2.getProfile()
                S3 = ki3.getProfile()
                S4 = ki4.getProfile()
                S5 = ki5.getProfile()
                S6 = ki6.getProfile()
                S7 = ki7.getProfile()
                ki.sendText(msg.to, S1.displayName + " ")
                ki2.sendText(msg.to, S2.displayName + " ")
                ki3.sendText(msg.to, S3.displayName + " ")
                ki4.sendText(msg.to, S4.displayName + " ")
                ki5.sendText(msg.to, S5.displayName + " ")
                ki6.sendText(msg.to, S6.displayName + " ")
                ki7.sendText(msg.to, S7.displayName + " ")

#--------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'Mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    kontak = cl.getContacts(blacklist)
                num=1
                msgs="User Black List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blacklist user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
                    #mc = ""
                    #for mi_d in wait["blacklist"]:
                        #mc += "�" +cl.getContact(mi_d).displayName + "\n"
                    #cl.sendText(msg.to,mc)                    
            elif msg.text.lower() == 'clear ban':
                wait["blacklist"] = {}
                cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Unbanned Success")

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = "✃┈┈[Blacklist]┈┈✍\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Cekban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "✃┈[Blacklist]┈✍"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to, cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user")
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text in ["Cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
            elif "Fakecat’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&amp;%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#-----------------------------------------------------------
            elif "Bc: " in msg.text:
	          if msg.from_ in admin:
	           	   bctxt = msg.text.replace("Bc: ","")
		           A = cl.getProfile()
		           n = cl.getGroupIdsJoined()
		           for manusia in n:
			       cl.sendText(manusia, (bctxt) + "\n\nʙʀᴏᴀᴅᴄᴀsᴛ ʙʏ : " + (A.displayName))
#-----------------------------------------------
            elif "Gbc " in msg.text:
		            bc = msg.text.replace("Gbc ","")
		            gid = cl.getGroupIdsJoined()
		            for i in gid:
		                cl.sendText(i,"====ɮʀօǟɖƈǟֆȶ ʍɛֆֆǟɢɛ====\n\n"+bc+"\n\n")
		            cl.sendText(msg.to,"s̲u̲c̲c̲e̲s̲s̲")            
#------------------------------------------------
#-----------------------------------------------
            elif msg.text in ["BTS in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.sendText(msg.to,"􀜁􀇔�Hello  "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "Mem in"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
        
            elif msg.text in ["Jungkook in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Jin in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki2.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki2.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Jimin in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki3.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki3.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["V in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki4.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki4.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Jhope in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki5.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki5.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Suga in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki6.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki6.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Rapmon in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki7.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki7.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)
#-----------------------------------------------
            elif "BTS out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to, "Keluar Bego")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye jungkook"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"􀜁􀇔�Bye Bye  "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye jin"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.sendText(msg.to,"􀜁􀇔�Bye Bye  "  +  str(ginfo.name)  + "")
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye jimin"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.sendText(msg.to,"􀜁􀇔�Bye Bye  "  +  str(ginfo.name)  + "")
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye v"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.sendText(msg.to,"􀜁􀇔�Bye Bye  "  +  str(ginfo.name)  + "")
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye jhope"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.sendText(msg.to,"􀜁􀇔�Bye Bye  "  +  str(ginfo.name)  + "")
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye suga"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.sendText(msg.to,"􀜁􀇔�Bye Bye  "  +  str(ginfo.name)  + "")
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye rapmon"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.sendText(msg.to,"􀜁􀇔�Bye Bye  "  +  str(ginfo.name)  + "")
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Bye me"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kam","Wc"]:
                  ginfo = cl.getGroup(msg.to)
                  cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                  cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Say " in msg.text:
				  bctxt = msg.text.replace("Say ","")
				  ki.sendText(msg.to,(bctxt))
				  ki2.sendText(msg.to,(bctxt))
				  ki3.sendText(msg.to,(bctxt))
				  ki4.sendText(msg.to,(bctxt))
				  ki5.sendText(msg.to,(bctxt))
				  ki6.sendText(msg.to,(bctxt))
#=========================================
            elif msg.from_ in mimic["target"] and mimic["copy"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		ki.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			ki.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            elif msg.text in ["Mimic on","mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off","mimic:off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Targetlist"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic set to " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#=======================================
            elif "Spam " in msg.text:
              if msg.from_ in Bots or staff:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 100:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
            elif msg.text in ["Speed"]:
            	if msg.from_ in Bots or staff:
                  start = time.time()
                  cl.sendText(msg.to, "Wait...")
                  elapsed_time = time.time() - start
                  cl.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up􏿿" % (elapsed_time))
            elif msg.text in ["BTSspeed"]:
            	if msg.from_ in Bots or staff:
                  start = time.time()
                  cl.sendText(msg.to, "Progress...")
                  elapsed_time = time.time() - start
                  ki.sendText(msg.to, "%s second" % (elapsed_time))
                  ki2.sendText(msg.to, "%s second" % (elapsed_time))
                  ki3.sendText(msg.to, "%s second" % (elapsed_time))
                  ki4.sendText(msg.to, "%s second" % (elapsed_time))
                  ki5.sendText(msg.to, "%s second" % (elapsed_time))
                  ki6.sendText(msg.to, "%s second" % (elapsed_time))
            elif msg.text in ["Sp"]:
	      if msg.from_ in admin:
                start = time.time()
		cl.sendText(msg.to, "「ᴅᴇʙᴜɢ sᴘᴇᴇᴅ」\nsᴘᴇᴇᴅ ɪᴛ's sᴛᴀʀᴛɪɴɢ♪\n ᴀʙᴏʀᴛ ᴛᴏ ᴀʙᴏʀᴛ♪")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "「ᴅᴇʙᴜɢ sᴘᴇᴇᴅ」\nᴛʏᴘᴇ : sᴘᴇᴇᴅ\nᴛɪᴍᴇ ᴛᴀᴋᴇɴ : %ssᴇᴄᴏɴᴅs♪♪" % (elapsed_time))
#----------------------------------------------- 
            elif msg.text in "Cium":
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#-----------------------------------------------
            elif msg.text.lower() in ["Cipok"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                    cnt = Message()
                    cnt.text = "Done : " + str(jml) +  " Members"
                    cnt.to = msg.to
                    cl.sendMessage(cnt)
#-----------------------------------------------
            elif "Searchid: " in msg.text:
                msgg = msg.text.replace('Searchid: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)
#============Auto respond=================
            elif "Mention on" in msg.text:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Detect Mention ON")
                
            elif "Mention off" in msg.text:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Detect Mention OFF")
#============Auto respond=================
#------------------------------------------------------------------	
            elif "Steal cover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
#--------------------------------steal BY Dp----------------------------------
            elif "Steal pict @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal pict @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
           
            elif "Steal group" in msg.text or "steal group" in msg.text:
                cc = cl.getGroup(msg.to)
                grup = "http://dl.profile.line-cdn.net/" + cc.pictureStatus
                cl.sendImageWithURL(msg.to,grup)
#------------------------------------------------------------------
#----------------Mayhem---------------#
            elif "Mayhem" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n' abort' to abort♪")
                    ki.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul•la•ba•loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done")
#----------------Mayhem---------------#
        if op.type == 19:
                if op.param3 in Bots:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 not in Bots:
                    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                if op.param2 in wait["whitelist"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        gs = ki3.getGroup(op.param1)
                        gs = ki4.getGroup(op.param1)
                        gs = ki5.getGroup(op.param1)
                        gs = ki6.getGroup(op.param1)
                        gs = ki7.getGroup(op.param1)
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
                        klist=[cl.ki,ki2,ki3,ki4,ki5,ki6,ki7]
                        kicker=random.choice(klist)
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protect"] == True:  
                   try:
                       klist=[ki.ki2.ki3.ki4.ki5.ki6,ki7]
                       kicker=random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       ki7.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kicker.updateGroup(X)
                       ki7.leaveGroup(op.param1)
                   except Exception, e:
                            print e
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Bots:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        #ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                if op.param3 in kimid:
                    if op.param2 in Bots:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)


                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)

                if op.param3 in ki3mid:
                    if op.param2 in Bots:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                if op.param3 in ki2mid:
                    if op.param2 in Bots:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                if op.param3 in ki4mid:
                    if op.param2 in Bots:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                if op.param3 in ki5mid:
                    if op.param2 in Bots:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                if op.param3 in ki6mid:
                    if op.param2 in Bots:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                if op.param3 in ki7mid:
                    if op.param2 in Bots:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(DEF).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki.updateGroup(G)
			random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(DEF).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(DEF).updateGroup(G)
			    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki2.kickoutFromGroup(op.param1,[op.param2])
		else:
		    ki2.sendText(op.param1,"")
	    else:
		ki2.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki3.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    ki3.sendText(op.param1,"")
	    else:
		ki3.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    ki.sendText(op.param1,"")
	    else:
		ki.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    Ticket = ki.reissueGroupTicket(op.param1)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki7.kickoutFromGroup(op.param1,[op.param2])
                    ki.updateGroup(G)
                    ki7.leaveGroup(op.param1)
                    ki.senText(msg.to,"Please Dont open Qr")
                if op.param2 in wait["blacklist"]:
                    pass
               # if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
		#elif wait["linkprotect"] == True:
		    #wait ["blacklist"][op.param2] = True
		    #G = cl.getGroup(op.param1)
		    #G.preventJoinByTicket = False
		    #cl.updateGroup(G)
		    #Ticket = cl.reissueGroupTicket(op.param1)
		    #ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
		    #X = cl.getGroup(op.param1)             
            #X.preventJoinByTicket = True
            #cl.updateGroup(X)
		    #ki7.kickoutFromGroup(op.param1,[op.param2])
		    #cl.updateGroup(X)
            #ki7.leaveGroup(op.param1)
		#else:
		    #cl.sendText(op.param1,"")
	    #else:
		#cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

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
                   ki2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki7.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki8.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki6.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki7.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki8.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenttar"])
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
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"[%H:%M]")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
        #if op.type == 59:
            #print op


    #except Exception as error:
        #print error


#def a2():
    #now2 = datetime.now()
    #nowT = datetime.strftime(now2,"%M")
    #if nowT[14:] in ["10","20","30","40","50","00"]:
        #return False
    #else:
        #return True
#def nameUpdate():
    #while True:
        #try:
        ##while a2():
            ##pass
            #if wait["clock"] == True:
                #now2 = datetime.now()
                #nowT = datetime.strftime(now2,"༺%H:%M༻")
                #profile = cl.getProfile()
                #profile.displayName = wait["cName"] + nowT
                #cl.updateProfile(profile)
            #time.sleep(600)
        #except:
            #pass
#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

#def autolike():
     #for zx in range(0,50):
        #hasil = cl.activity(limit=1000)
        #if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          #try:    
            #cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rio_S✈ \nhttp://line.me/ti/p/~ilssc")
            #ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rio_S✈")
            #kii2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rio_S✈")
            #ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rio_S✈")
            #ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rio_S✈")
            #ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rio_S✈")
            #ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Rio_S✈")
            #ki7.ike(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki7.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by CommelL Chuta✈")
            
            
            
            
            
            #print "Like"
          #except:
            #pass
        #else:
            #print "Already Liked"
     #time.sleep(600)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

#"filter":false,"title":"jst.py","tooltip":"/Destroyer/InoriYuzuhira/jst.py","undoManager":{"mark":-1,"position":-1,"stack":[]},"ace":{"folds":[],"scrolltop":3234.877176321621,"scrollleft":-40,"selection":{"start":{"row":214,"column":62},"end":{"row":214,"column":62},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":226,"state":"start","mode":"ace/mode/python"}},"timestamp":1512039493859,"hash":"5ae508637e73399bf5c8490a68b4b2e7d11b2307"}{"filter":false,"title":"jst.py","tooltip":"/Defender/jst.py","undoManager":{"mark":-1,"position":-1,"stack":[]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0}