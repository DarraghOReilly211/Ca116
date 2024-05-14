#!/usr/bin/env python3

import sys

i = 0
with open("input.txt") as f:
   s = f.read()
t = ""
while i < len(s):
   if (s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z"):
      t = t + "*"
   else:
      t = t + s[i]
   i = i + 1
with open("output.txt", "w") as f:
   f.write(t)
