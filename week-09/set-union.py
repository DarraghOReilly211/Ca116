#!/usr/bin/env python3

import sys
union = {}

with open("a.txt") as f:
   s = f.readline().strip()
   #print(s)
   while 0 < len(s):
      union[s] = True
      s = f.readline().strip()
#print(union)
with open("b.txt") as f:
   s = f.readline().strip()
   while 0 < len(s):
      if s not in union:
         union[s] = True
      s = f.readline().strip()
#print(union)

for s in union:
   print(s)
