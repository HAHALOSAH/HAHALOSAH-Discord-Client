#!/usr/bin/python3
########################
# Written by HAHALOSAH #
########################
import requests
import json
import getpass
baseURL = "https://discordapp.com/api/v8/auth/login"
headers = { "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Content-Type":"application/json"}
email = input("Email: ")
password = getpass.getpass("Password: ")
POSTedJSON =  json.dumps ( {"email": email, "password": password} )

r = requests.post(baseURL, headers = headers, data = POSTedJSON)
print(r.status_code)
result = json.loads(r.text)
#print(r.text)
if r.status_code == 200:
  f = open("token.txt", "w")
  f.write(result["token"])
  f.close()
  print("--LOGGED IN--")
  exec(open('startup.py').read())
elif r.status_code == 400:
  print("Password does not match! (Bad Password)")
  exec(open('login.py').read())
else:
  print("Error " + str(r.status_code) + ": " + r.text)
