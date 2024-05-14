#!/usr/bin/env python3

a = []
s = input()

while s != "end":
   token = " ".join(s.split())
   a.append(token)
   s = input()

day = input()

i = 0
while i < len(a):
   if (a[i])[0] == day:
      print(" ".join((a[i].split())))
   i = i + 1
