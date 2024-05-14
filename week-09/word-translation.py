#!/usr/bin/env python3

import sys

translations = {}
i = 0
with open("translation.txt") as f:
   s = f.readline().split()
   while 0 < len(s):
      #print(s)
      translations[s[0]] = s[1]
      s = f.readline().split()
#print(translations)

s = sys.stdin.readline().strip()
while 0 < len(s):
   print(translations[s])
   s = sys.stdin.readline().strip()
