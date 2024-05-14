#!/usr/bin/env python3

s = (input())
i = 0

while i < len(s):
   if len(s) * " " == s:
      print(-1)
      i = len(s)
   elif "a" <= s[i] <= "z" or "A" <= s[i] <= "Z" or s[i] == "_":
      print(i)
      i = len(s)
   else:
      i = i + 1
