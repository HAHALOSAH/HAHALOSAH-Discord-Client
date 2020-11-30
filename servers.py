#!/usr/bin/python3
########################
# Written by HAHALOSAH #
########################
import requests
import json
f = open("token.txt", "r")
token = f.read()
f.close()
baseURL = "https://discordapp.com/api/v8/users/@me/guilds"
headers = { "Authorization": token, "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
r = requests.get(baseURL, headers = headers)
if r.status_code == 200:
  #print(r.text)
  f = open("servers.json", "w")
  f.write(r.text)
  f.close()
  #print("Updated Servers List")
else:
  print("Error " + str(r.status_code) + ": " + r.text)

