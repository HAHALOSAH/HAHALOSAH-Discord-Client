#!/usr/bin/python3
########################
# Written by HAHALOSAH #
########################
import requests
import json
f = open("token.txt", "r")
token = f.read()
f.close()
baseURL = "https://discord.com/api/users/715423848358608896"
headers = { "Authorization": token, "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Content-Type":"application/json"}
POSTedJSON = "{\"provider\":null,\"voip_provider\":null}" # json.dumps ( {"provider":null,"voip_provider":null} )
r = requests.get(baseURL, headers = headers)
print(r.status_code)
if r.status_code == 204:
  print(r.text)
  f = open("userinfo.json", "w")
  f.write("--USER LOGGED OUT--")
  f.close()
  f = open("token.txt", "w")
  f.write("--USER LOGGED OUT--")
  f.close()
  print("Successfully Logged Out")
else:
  print("Error " + str(r.status_code) + ": " + r.text)


