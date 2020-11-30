#!/usr/bin/python3
########################
# Written By HAHALOSAH #
########################
import requests
import json
import os.path
import readline
selectedchannel = ""
selectedserver = ""
f = open("token.txt", "r")
token = f.read()
f.close()
baseURL = "https://discordapp.com/api/v8/users/@me"
headers = { "Authorization": token, "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Content-Type":"application/json"}

r = requests.get(baseURL, headers = headers)
#print(r.status_code)
result = json.loads(r.text)
if r.status_code == 200:
  #print(r.text)
  f = open("userinfo.json", "w")
  f.write(r.text)
  f.close()
  user = json.loads(open("userinfo.json").read())
  exec(open("servers.py").read())
  print("Welcome back, " + user["username"])
  exec(open("prompt.py").read())
else:
  exec(open('login.py').read())

