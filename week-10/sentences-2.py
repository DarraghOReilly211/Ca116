#!/usr/bin/env python3

import sys

s = sys.stdin.read().split()

cap = ""
map = {
   ".": True,
   "!": True,
   "?": True,
}
t = ""
i = 0
while i < len(s):
   j = i
   while j < len(s) and s[j][len(s[j]) - 1] not in map:
      j = j + 1

   j = j + 1
   if ("Z" < s[i][0] and s[i][0] > "A"):
      cap = s[i]
      cap = cap.capitalize()
   else:
      cap = s[i]
   t = " ".join(s[i + 1:j])
   sys.stdout.write(cap + " ")
   print(t)
   i = j
