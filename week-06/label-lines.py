#!/usr/bin/env python3

a = []
s = input()
a.append(s)
while s != "end":
   s = input()
   a.append(s)
i = 0
while i < (len(a) - 1):
   print((i), (len(a) - 1), a[i])
   i = i + 1
