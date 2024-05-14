#!/usr/bin/env python3

s = str(input())
i = 0
r = ""
while i < len(s):
   if s[i] != " ":
      r = r + s[i]
      i = i + 1
   else:
      i = i + 1
print(r)
