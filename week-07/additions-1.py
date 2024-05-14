#!/usr/bin/env python3

i = 0
j = 0
while i < 10:
   j = 0
   s = str(input())
   while j < len(s):
      if s[j] != "+":
         j = j + 1
      else:
         n = j
         print(int(s[:n]) + int(s[n:]))
         j = len(s)
   i = i + 1
