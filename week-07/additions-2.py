#!/usr/bin/env python3

i = 0
j = 0
n = 0
s = str(input())
while i < len(s):
   if s[i] != "+":
      i = i + 1
   else:
      n = n + int(s[j:i])
      #print(n)
      j = i + 1
      i = i + 1
n = n + int(s[j:])

i = 0
while i != len(s):
   print(n)
   i = len(s)
