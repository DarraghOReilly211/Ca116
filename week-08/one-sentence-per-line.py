#!/usr/bin/env python3

a = []
s = input()

while s != "end":
   a.append(s)
   s = input()

s = " ".join(a)
a = s.split()
s = " ".join(a)
a = s.split(".")

i = 0
while i < len(a) - 1:
   print((a[i] + ".").lstrip())
   i = i + 1
