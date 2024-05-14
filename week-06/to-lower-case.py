#!/usr/bin/env python3

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"

s = input()
while s != "end":
   i = 0
   out = ""
   while i < len(s):
      j = 0
      while j < len(upper) and s[i] != upper[j]:
         j = j + 1
      if j < len(upper):
         out = out + lower[j]
      else:
         out = out + s[i]
      i = i + 1
   print(out)
   s = input()
