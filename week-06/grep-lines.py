#!/usr/bin/env python3

import sys

args = sys.argv

pattern = args[1]

s = input()
i = 0

while s != "end":
   i = 0
   while i < len(s) and (s[i:i + len(pattern)] != pattern):
      i = i + 1
   if i < len(s):
      print(s)
   s = input()

