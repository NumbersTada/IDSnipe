from distutils.command.upload import upload
import time,requests,random,os,base64,hashlib
from itertools import cycle
from urllib3 import connection
from json import loads
from threading import Thread

def request(self, method, url, body=None, headers=None):
    if headers is None:
        headers = {}
    else:
        headers = headers.copy()
    super(connection.HTTPConnection, self).request(method, url, body=body, headers=headers)
connection.HTTPConnection.request = request

def comment_chk(*,username,comment,levelid,percentage,type):
        part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
        return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()
def generate_chk(values: [int, str] = [], key: str = "", salt: str = "") -> str:
    values.append(salt)

    string = ("").join(map(str, values))

    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor(hashed, key)
    final = base64.urlsafe_b64encode(xored.encode()).decode()

    return final
def generate_upload_seed(data: str, chars: int = 50) -> str:
    if len(data) < chars:
        return data
    step = len(data) // chars
    return data[::step][:chars]
def xor(data, key):
        return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
def gjp_encrypt(data):
        return base64.b64encode(xor(data,"37526").encode()).decode()
def gjp_decrypt(data):
        return xor(base64.b64decode(data.encode()).decode(),"37526")

def getGJUsers(target):
    data={
        "secret":"Wmfd2893gb7",
        "str":target
    }
    request =  requests.post("http://www.boomlings.com/database/getGJUsers20.php",data=data,headers={"User-Agent": ""}).text.split(":")[1::2]
    username = request[0]
    uuid = request[2]
    accountid = request[10]
    return (username,accountid,uuid)

def fetchID():
    data={
        "gameVersion":"21",
        "binaryVersion":"35",
        "gdw":"0",
        "type":"4",
        "str":"",
        "diff":"-",
        "len":"-",
        "page":"0",
        "total":"0",
        "uncompleted":"0",
        "onlyCompleted":"0",
        "featured":"0",
        "original":"0",
        "twoPlayer":"0",
        "coins":"0",
        "epic":"0",
        "secret":"Wmfd2893gb7"
    }
    fetched = requests.post("http://www.boomlings.com/database/getGJLevels21.php",data=data,headers={"User-Agent": ""}).text
    return fetched.split(":")[1]

def uploadGJLevel(name,passw,levelString,lvlName,desc,ver,length,audio,password,original,twoP,songID,objects,coins,reqStars,unlisted,ldm):
    data = {
        "gameVersion": 21,
        "accountID": getGJUsers(name)[1],
        "gjp": gjp_encrypt(passw),
        "userName": name,
        "levelID": 0,
        "levelName": lvlName,
        "levelDesc": base64.b64encode(desc.encode()).decode(),
        "levelVersion": int(ver),
        "levelLength": int(length),
        "audioTrack": int(audio),
        "auto": 0,
        "password": int(password),
        "original": int(original),
        "twoPlayer": int(twoP),
        "songID": int(songID),
        "objects": int(objects),
        "coins": int(coins),
        "requestedStars": int(reqStars),
        "unlisted": int(unlisted),
        "ldm": int(ldm),
        "levelString": levelString,
        "seed2": generate_chk(key="41274", values=[generate_upload_seed(levelString)], salt="xI25fpAapCQg"),
        "secret": "Wmfd2893gb7"
    }
    req = requests.post("http://www.boomlings.com/database/uploadGJLevel21.php", data=data, headers={"User-Agent":""})
    print(req.text)

lvlString = "H4sIAAAAAAAAC6WQwQ3DIAxFF3IlfxsIUU6ZIQP8AbJChy_GPSZqpF7-A4yfDOfhXcCiNMIqnVYrgYQl8rDwBTZCVbkQRI3oVHbiDU6F2jMF_lesl4q4kw2PJMbovxLBQxTpM3-I6q0oHmXjzx7N0240cu5w0UBNtESRkble8uSLHjh8nTubmYJZ2MvMrEITEN0gEJMxlLiMZ28frmj"

print(" /\_/\               IDSnipe v1.0")
print("( . . )            by NumbersTada")
print(">)-A-(< Get 100M level ID easily.")
print("---------------------------------")
print("[Loading]      Reading config.dat")
with open("config.dat", mode="r", encoding="utf-8") as configfile:
    config=configfile.read().split(";")
    username=config[0]
    password=config[1]
    lvlName1=config[2]
    lvlName2=config[3]
    lvlName3=config[4]
    lvlName4=config[5]
    lvlName5=config[6]
    snipingID=int(config[7])
print("[Message]      Successfully loaded.")
input("[Confirmation] Press ENTER to start sniping ID (using account "+username+").")


while True:
    fetchedID = int(fetchID())
    if fetchedID >= snipingID-5:
        if fetchedID >= snipingID+2:
            print("[Message]      Program ended.")
        else:
            uploadGJLevel(username,password,lvlString,lvlName1,"Posted using NumbersTada's IDSnipe!",69,0,0,1337420,69696969,1,1230110,42069,5,69,0,1)
            uploadGJLevel(username,password,lvlString,lvlName2,"Posted using NumbersTada's IDSnipe!",69,0,0,1337420,69696969,1,1230110,42069,5,69,0,1)
            uploadGJLevel(username,password,lvlString,lvlName3,"Posted using NumbersTada's IDSnipe!",69,0,0,1337420,69696969,1,1230110,42069,5,69,0,1)
            uploadGJLevel(username,password,lvlString,lvlName4,"Posted using NumbersTada's IDSnipe!",69,0,0,1337420,69696969,1,1230110,42069,5,69,0,1)
            uploadGJLevel(username,password,lvlString,lvlName5,"Posted using NumbersTada's IDSnipe!",69,0,0,1337420,69696969,1,1230110,42069,5,69,0,1)
