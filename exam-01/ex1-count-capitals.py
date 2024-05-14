#!/usr/bin/env python3

s = input()
r = ""

i = 0
while i < len(s):
   if "A" <= s[i] <= "Z":
      r = r + s[i]
   i = i + 1
print(len(r))
