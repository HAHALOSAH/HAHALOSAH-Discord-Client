#!/usr/bin/python3
########################
# Written by HAHALOSAH #
########################
import requests
import json
import os.path
import atexit
import readline
import rlcompleter
import re
historyPath = os.path.expanduser("~/.hhlscmdhistory")

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)
del os, atexit, readline, rlcompleter, save_history, historyPath
print("Welcome to HAHALOSAH-Discord-Client.")
print("For a list of commands type \"help\".")
print("Press Ctrl-C to quit, or type \"exit\" to quit.")
while (1):
  try:
    cmd = input(">>> ").strip()
    if cmd == "exit":
      exit()
    elif cmd == "":
      continue
    #elif cmd == "select":
    #  if cmd.split()[1] == "server":
    #    server = cmd.split()[2]
    #  if cmd.split()[1] == "channel":
    #    server = cmd.split()[2]
    f = open("token.txt", "r")
    token = f.read()
    f.close()
    f = open("userinfo.json", "r")
    user = json.loads(f.read())
    f.close()
    f = open("servers.json", "r")
    servers = json.loads(f.read())
    f.close()
    args = re.sub("\\\\;", " ", re.sub(" ", ";", cmd)).split(";")
    #exec(open("servers.py").read())
    #exec(open("update-info.py").read())
    import os.path
    if os.path.isfile("cmds/" + args[0]):
      if len(args) == 3:
        exec("parama = \"" + args[1] + "\"\nparamb = \"" + args[2] + "\"\n" + open("cmds/" + args[0]).read())
      elif len(args) == 2:
        exec("parama = \"" + args[1] + "\"\nparamb = \"\"\n" + open("cmds/" + args[0]).read())
      else:
        exec("parama = \"\"\nparamb = \"\"\n" + open("cmds/" + args[0]).read())
    else:
      print("Invalid command: " + cmd + ". For a list of commands type \"help\".")
  except KeyboardInterrupt:
    print()
    exit()
