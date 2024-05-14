#!/usr/bin/env python3

import sys

n = sys.stdin.read()
n = n.split("\n")
#print(n)
i = 0
output = ""
while i < len(n):
   j = 0
   s = n[i]
   while j < len(s):
      if s[j] == "(":
         d = j + 1
      elif s[j] == ")":
         output = (output + s[d:j] + "\n")
         j = len(s)
      j = j + 1
   i = i + 1

if len(output) > 0:
   print(output.strip())
