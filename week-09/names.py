#!/usr/bin/env python3

import sys

names = {}
with open("boys.txt") as f:
   s = f.read()
   s = s.split()
   s = " ".join(s)
   s = s.rstrip("\n")
   s = s.split()

i = 0
while i < len(s):
   names[s[i]] = "boy"
   i = i + 1


with open("girls.txt") as f:
   s = f.read()
   s = s.split()
   s = " ".join(s)
   s = s.rstrip("\n")
   s = s.split()

i = 0
while i < len(s):
   if s[i] not in names:
      names[s[i]] = "girl"
   else:
         names[s[i]] = "either"
   i = i + 1

#print(names)
s = sys.stdin.readline().strip()
while 0 < len(s):
   print(s, names[s])
   s = sys.stdin.readline().strip()
