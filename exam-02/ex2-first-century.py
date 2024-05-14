#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
a = []

i = 0
while i < len(s):
   if 100 <= int(s[i]):
      a.append(s[i])
      i = i + 1
   else:
      i = i + 1

if len(a) == 0:
   print("none")
else:
   print(a[0].strip())
