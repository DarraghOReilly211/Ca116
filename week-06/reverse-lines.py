#!/usr/bin/env python3

s = input()
a = []
b = []
i = 0

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   tmp = a[len(a) - i - 1]
   b.append(tmp)
   i = i + 1

i = 0
while i < len(b):
   print(b[i])
   i = i + 1
