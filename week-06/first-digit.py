#!/usr/bin/env python3

s = (input())
i = 0

while i < len(s):
   if "a" <= s[i] <= "z" or s[i] == " ":
      i = i + 1
   else:
      print(s[i], i)
      i = len(s)
