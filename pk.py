from linepy import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, pytz, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse
_session = requests.session()
botStart = time.time()
listApp = [
	"CHROMEOS\t2.1.5\tKrisna\t0.18.1660.143.0"
	#"DESKTOPWIN\t5.9.2\tKrisna\t11.2.5", 
	#"DESKTOPMAC\t5.9.2\tKrisna\t11.2.5", 
	#"IOSIPAD\t8.14.2\tKrisna\t11.2.5", 
	#"WIN10\t5.5.5\tKrisna\t11.2.5"
]
for app in listApp:
    with open("authToken.txt", "r") as token:
        authToken = token.read().replace("\n","")
    if not authToken:
        kr = LINE()
        with open("authToken.txt","w") as token:
            token.write(kr.authToken)
        continue
    kr = LINE(authToken, appName=app)
    kr.log("Auth Token : " + str(kr.authToken))
    with open("authToken1.txt", "r") as token:
        authToken = token.read().replace("\n","")
    if not authToken:
        kr1 = LINE()
        with open("authToken1.txt","w") as token:
            token.write(kr1.authToken)
        continue
    kr1 = LINE(authToken, appName=app)
    kr1.log("Auth Token : " + str(kr1.authToken))
    with open("authToken2.txt", "r") as token:
        authToken = token.read().replace("\n","")
    if not authToken:
        kr2 = LINE()
        with open("authToken2.txt","w") as token:
            token.write(kr2.authToken)
        continue
    kr2 = LINE(authToken, appName=app)
    kr2.log("Auth Token : " + str(kr2.authToken))
    with open("authToken3.txt", "r") as token:
        authToken = token.read().replace("\n","")
    if not authToken:
        kr3 = LINE()
        with open("authToken3.txt","w") as token:
            token.write(kr3.authToken)
        continue
    kr3 = LINE(authToken, appName=app)
    kr3.log("Auth Token : " + str(kr3.authToken))
    with open("authToken4.txt", "r") as token:
        authToken = token.read().replace("\n","")
    if not authToken:
        kr4 = LINE()
        with open("authToken4.txt","w") as token:
            token.write(kr4.authToken)
        continue
    kr4 = LINE(authToken, appName=app)
    kr4.log("Auth Token : " + str(kr4.authToken))
    with open("authToken5.txt", "r") as token:
        authToken = token.read().replace("\n","")
    if not authToken:
        kr5 = LINE()
        with open("authToken5.txt","w") as token:
            token.write(kr5.authToken)
        continue
    kr5 = LINE(authToken, appName=app)
    kr5.log("Auth Token : " + str(kr5.authToken))
    break
print ("LOGIN SUCCESS PK CYBER ARMY BOT")
oepoll = OEPoll(kr)
lineProfile = kr.getProfile()
lineSettings = kr.getSettings()
krMID = kr.profile.mid
kr1MID = kr1.getProfile().mid
kr2MID = kr2.getProfile().mid
kr3MID = kr3.getProfile().mid
kr4MID = kr4.getProfile().mid
kr5MID = kr5.getProfile().mid
mid = kr.getProfile().mid
Bots = [krMID,kr1MID,kr2MID,kr3MID,kr4MID,kr5MID]
Owner=["u35459f1e84ad208cc56025c259cb1628","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
admin=["u9cc2323f5b84f9df880c33aa9f9e3ae1","u35459f1e84ad208cc56025c259cb1628"]
protectkick = []
protectcancel = []
settings = {
    "blacklist": {}
}
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    kr.log("[ ERROR ] " + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("Error.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def help():
    with open('help.txt', 'r') as f:
        text = f.read()
    helpMsg = text
    return helpMsg
def command(text):
    pesan = text.lower()
    krtext = text.lower()
    return krtext
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kr.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        krtext = command(text)
                        if krtext == "pk keys":
                            if sender in Owner:
                                kr.sendMessage(to, str(help()))
                        elif krtext == "pk speed":
                            if sender in Owner:
                                start = time.time()
                                kr.sendMessage(to, "Prosses...")
                                elapsed_time = time.time() - start
                                kr.sendMessage(to,format(str(elapsed_time)))
                        if krtext == "pk masuk":
                            if sender in Owner:
                                anggota = [kr1MID,kr2MID,kr3MID,kr4MID,kr5MID]
                                kr.inviteIntoGroup(msg.to, anggota)
                                kr1.acceptGroupInvitation(msg.to)
                                kr2.acceptGroupInvitation(msg.to)
                                kr3.acceptGroupInvitation(msg.to)
                                kr4.acceptGroupInvitation(msg.to)
                                kr5.acceptGroupInvitation(msg.to)
                        elif krtext == "pk asup":
                            if sender in Owner:
                                try:
                                    G = kr.getGroup(to)
                                    G.preventedJoinByTicket = False
                                    kr.updateGroup(G)
                                    Ticket = kr.reissueGroupTicket(to)
                                    kr1.acceptGroupInvitationByTicket(to,Ticket)
                                    kr2.acceptGroupInvitationByTicket(to,Ticket)
                                    kr3.acceptGroupInvitationByTicket(to,Ticket)
                                    kr4.acceptGroupInvitationByTicket(to,Ticket)
                                    kr5.acceptGroupInvitationByTicket(to,Ticket)
                                except:
                                    pass
                        elif krtext.startswith("pk cium "):
                            if sender in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            kr1.kickoutFromGroup(to,[ls])
                                            print (to,[ls])
                                        except:
                                            try:
                                                kr2.kickoutFromGroup(to,[ls])
                                                print (to,[ls])
                                            except:
                                                try:
                                                    kr3.kickoutFromGroup(to,[ls])
                                                    print (to,[ls])
                                                except:
                                                    kr4.kickoutFromGroup(to,[ls])
                                                    print (to,[ls])
                        elif krtext == "banlist":
                            if sender in Owner or admin:
                                if settings["blacklist"] == {}:
                                    kr.sendMessage(to,"Tidak Ada kontak blacklist")
                                else:
                                    kr.sendMessage(to,"═══════List blacklist═══════")
                                    h = ""
                                    for i in settings["blacklist"]:
                                        h = kr.getContact(i)
                                        kr.sendContact(to,i)
                        elif krtext == "clearban":
                            if sender in Owner or admin:
                                settings["blacklist"] = {}
                                kr.sendMessage(to,"success to clear blacklist..!!")
                        elif krtext == "pk bot" or krtext == "mybot":
                            if sender in Owner:
                                kr.sendContact(to, krMID)
                                kr.sendContact(to, kr1MID)
                                kr.sendContact(to, kr2MID)
                                kr.sendContact(to, kr3MID)
                                kr.sendContact(to, kr4MID)
                                kr.sendContact(to, kr5MID)
                        elif krtext == "pk cek":
                            if sender in Owner:
                                profile = kr1.getProfile()
                                text = profile.displayName + (" Siap Nyabun..!!")
                                kr1.sendMessage(to, text)
                                profile = kr2.getProfile()
                                text = profile.displayName + (" Siap Ngocok..!!")
                                kr2.sendMessage(to, text)
                                profile = kr3.getProfile()
                                text = profile.displayName + (" Siap Nyodok..!!")
                                kr3.sendMessage(to, text)
                                profile = kr4.getProfile()
                                text = profile.displayName + (" Siap Nikung..!!")
                                kr4.sendMessage(to, text)
                                profile = kr5.getProfile()
                                text = profile.displayName + (" Siap Kojom..!!")
                                kr5.sendMessage(to, text)
                                kr.sendMessage(to,"Pasukan Kemeng Ready..!!")
                        elif krtext == "pk bye":
                            if sender in Owner:
                                kr1.leaveGroup(msg.to)
                                kr2.leaveGroup(msg.to)
                                kr3.leaveGroup(msg.to)
                                kr4.leaveGroup(msg.to)
                                kr5.leaveGroup(msg.to)
                                kr.leaveGroup(msg.to)
                        elif krtext == "pk kabur":
                            if sender in Owner:
                                kr1.leaveGroup(msg.to)
                                kr2.leaveGroup(msg.to)
                                kr3.leaveGroup(msg.to)
                                kr4.leaveGroup(msg.to)
                                kr5.leaveGroup(msg.to)
                        elif krtext.startswith("pk kemeng "):
                            if sender in Owner:
                                spl = krtext.replace("pk kemeng ","")
                                if spl == 'on':
                                    if msg.to in protectkick:
                                        msgs = ""
                                    else:
                                        protectkick.append(msg.to)
                                    if msg.to in protectcancel:
                                        ginfo = kr.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                        msgs += "\nMode kemeng diaktifkan"
                                    else:
                                        protectcancel.append(msg.to)
                                        ginfo = kr.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                        msgs += "\nMode kemeng diaktifkan"
                                    kr.sendMessage(msg.to, "「 Status Kemeng on 」\n" + msgs)
                                elif spl == 'off':
                                    if msg.to in protectkick:
                                        protectkick.remove(msg.to)
                                    else:
                                        msgs = ""
                                    if msg.to in protectcancel:
                                        protectcancel.remove(msg.to)
                                        ginfo = kr.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                        msgs += "\nMode kemeng dimatikan"
                                    else:
                                        ginfo = kr.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                        msgs += "\nMode kemeng dimatikan"
                                    kr.sendMessage(msg.to, "「 Status Kemeng off 」\n" + msgs)
                        elif krtext == "pk ancur":
                            if sender in Owner:
                                if msg.toType == 2:
                                    gs = kr.getGroup(msg.to)
                                    gs = kr1.getGroup(msg.to)
                                    gs = kr2.getGroup(msg.to)
                                    gs = kr3.getGroup(msg.to)
                                    gs = kr4.getGroup(msg.to)
                                    gs = kr5.getGroup(msg.to)
                                    time.sleep(0.0002)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        kr.sendMessage(to,"LIMIT.!!!")
                                    else:
                                        for target in targets:
                                            if target not in Bots:
                                                if target not in Owner:
                                                    if target not in admin:
                                                        try:
                                                            klist=[kr1,kr2,kr3,kr4,kr5]
                                                            kicker=random.choice(klist)
                                                            kicker.kickoutFromGroup(to,[target])
                                                            print (to,[g.mid])
                                                        except:
                                                            pass
        if op.type == 19 or op.type == 32:
            if krMID in op.param3:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    kr1.inviteIntoGroup(op.param1,[op.param3])
                    kr.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                            kr.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                                kr.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr4.inviteIntoGroup(op.param1,[op.param3])
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                    kr.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kr5.inviteIntoGroup(op.param1,[op.param3])
                                        kr5.kickoutFromGroup(op.param1,[op.param2])
                                        kr.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = kr1.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kr1.updateGroup(G)
                                            Ticket = kr1.reissueGroupTicket(op.param1)
                                            kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr1.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            G = kr2.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kr2.updateGroup(G)
                                            Ticket = kr2.reissueGroupTicket(op.param1)
                                            kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr2.kickoutFromGroup(op.param1,[op.param2])
                return
            if kr1MID in op.param3:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    kr.inviteIntoGroup(op.param1,[op.param3])
                    kr1.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr2.inviteIntoGroup(op.param1,[op.param3])
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                        kr1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr3.inviteIntoGroup(op.param1,[op.param3])
                            kr3.kickoutFromGroup(op.param1,[op.param2])
                            kr1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr4.inviteIntoGroup(op.param1,[op.param3])
                                kr4.kickoutFromGroup(op.param1,[op.param2])
                                kr1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr5.inviteIntoGroup(op.param1,[op.param3])
                                    kr5.kickoutFromGroup(op.param1,[op.param2])
                                    kr1.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = kr.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kr.updateGroup(G)
                                        Ticket = kr.reissueGroupTicket(op.param1)
                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if kr2MID in op.param3:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    kr.inviteIntoGroup(op.param1,[op.param3])
                    kr2.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr3.inviteIntoGroup(op.param1,[op.param3])
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr4.inviteIntoGroup(op.param1,[op.param3])
                            kr4.kickoutFromGroup(op.param1,[op.param2])
                            kr2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr5.inviteIntoGroup(op.param1,[op.param3])
                                kr5.kickoutFromGroup(op.param1,[op.param2])
                                kr2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr1.inviteIntoGroup(op.param1,[op.param3])
                                    kr1.kickoutFromGroup(op.param1,[op.param2])
                                    kr2.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = kr.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kr.updateGroup(G)
                                        Ticket = kr.reissueGroupTicket(op.param1)
                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr2.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if kr3MID in op.param3:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    kr.inviteIntoGroup(op.param1,[op.param3])
                    kr3.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr4.inviteIntoGroup(op.param1,[op.param3])
                        kr4.kickoutFromGroup(op.param1,[op.param2])
                        kr3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr5.inviteIntoGroup(op.param1,[op.param3])
                            kr5.kickoutFromGroup(op.param1,[op.param2])
                            kr3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr1.inviteIntoGroup(op.param1,[op.param3])
                                kr1.kickoutFromGroup(op.param1,[op.param2])
                                kr3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr2.inviteIntoGroup(op.param1,[op.param3])
                                    kr2.kickoutFromGroup(op.param1,[op.param2])
                                    kr3.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = kr.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kr.updateGroup(G)
                                        Ticket = kr.reissueGroupTicket(op.param1)
                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr3.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if kr4MID in op.param3:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    kr.inviteIntoGroup(op.param1,[op.param3])
                    kr4.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr5.inviteIntoGroup(op.param1,[op.param3])
                        kr5.kickoutFromGroup(op.param1,[op.param2])
                        kr4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr1.inviteIntoGroup(op.param1,[op.param3])
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                            kr4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr2.inviteIntoGroup(op.param1,[op.param3])
                                kr2.kickoutFromGroup(op.param1,[op.param2])
                                kr4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr3.inviteIntoGroup(op.param1,[op.param3])
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                                    kr4.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = kr.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kr.updateGroup(G)
                                        Ticket = kr.reissueGroupTicket(op.param1)
                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if kr5MID in op.param3:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    kr.inviteIntoGroup(op.param1,[op.param3])
                    kr5.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                            kr5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                                kr5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr4.inviteIntoGroup(op.param1,[op.param3])
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                    kr5.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = kr.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kr.updateGroup(G)
                                        Ticket = kr.reissueGroupTicket(op.param1)
                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if op.param3 in Owner or op.param3 in admin:
                if op.param2 not in Bots or op.param2 not in Owner or op.param2 not in admin:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr4.inviteIntoGroup(op.param1,[op.param3])
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kr5.inviteIntoGroup(op.param1,[op.param3])
                                        kr5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
        if op.type == 17:
            if op.param1 in protectkick:
                if op.param2 in settings["blacklist"]:
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kr5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
        if op.type == 13:
            if krMID in op.param3:
                if op.param2 in Bots or op.param2 in Owner:
                    kr.acceptGroupInvitation(op.param1)
            if op.param1 in protectkick:
                if op.param2 in settings["blacklist"]:
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kr5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots or op.param2 not in Owner or op.param2 not in admin:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                kr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            kr5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
    except Exception as error:
        logError(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        kr.log("[SINGLE_TRACE] ERROR : " + str(e))
