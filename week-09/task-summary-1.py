#!/usr/bin/env python3

import sys

programs = {}
s = sys.stdin.readline().strip()
while 0 < len(s):
   s = s.split(".")
   s[0] = s[0] + "." + s[1]
   s[1] = "." + s[2]
   s.pop()
   programs[s[0]] = s[1]
   s = sys.stdin.readline().strip()

for s in programs:
   if programs[s] == ".correct":
      print(s)
