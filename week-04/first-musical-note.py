#!/usr/bin/env python3

s = str(input())
i = 0

while i < len(s):
   if "a" <= s[i] <= "g":
      print(s[i])
      i = len(s)
   else:
      i = i + 1
