#!/usr/bin/env python3

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"
s = input()
while s != "end":
   i = 0
   j = 0
   while j < len(upper) and s[i] != upper[j]:
      j = j + 1
   if s[i] == upper[j]:
      s[i] = lower[j]
      j = 0
      i = i + 1
   elif j == len(upper):
      i = i + 1
   print(s)
   s = input()