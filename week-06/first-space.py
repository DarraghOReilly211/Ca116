#!/usr/bin/env python3
 
s = (input())
i = 0
 
while i < len(s):
   if s[i] == " ":
      print(i)
      i = len(s)
   elif "a" <= s[i] <= "z" or "A" <= s[i] <= "Z" or s[i] == "_":
      i = i + 1
   else:
      print("-1")
      i = len(s)