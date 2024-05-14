#!/usr/bin/env python3

import sys

dic = {
   "o": 0,
   "i": 0,
   "u": 0,
   "a": 0,
   "e": 0,
   "O": 0,
   "I": 0,
   "U": 0,
   "A": 0,
   "E": 0
}

s = sys.stdin.readlines()
i = 0
while i < len(s):
   j = 0
   d = s[i]
   while j < len(d):
      if d[j] in dic:
         dic[d[j]] = dic[d[j]] + 1
         j = j + 1
      else:
         j = j +1 
   i = i + 1

for d in dic:
   print(d, dic[d])
