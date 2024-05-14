#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

dictionary = {
   ".": True,
   ",": True,
   "!": True,
   "?": True,
   ";": True,
   ":": True,
   '"': True
}

total = 0
i = 0
while i < len(s):
   line = s[i]
   j = 0
   while j < len(s[i]):
      if line[j] in dictionary:
         total = total + 1
         j = j + 1
      else:
         j = j + 1
   i = i + 1

print(total)
