#!/usr/bin/python3
########################
# Written by HAHALOSAH #
########################
import requests
import json
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
  #print("User Info Updated")
else:
  print("Error " + str(r.status_code) + ": " + r.text)


