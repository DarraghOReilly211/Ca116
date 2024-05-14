#!/usr/bin/env python3

s = str(input())
i = 0

while i < len(s):
   if "A" <= s[i] <= "Z":
      print(i)
      i = len(s)
   else:
      i = i + 1
