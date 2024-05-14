#!/usr/bin/env python3

a = [0, 1, 1]

n = int(input())
i = 0
while i < n:
   b = (int(a[len(a) - 2]) + int(a[len(a) - 1]))
   a.append(b)
   i = i + 1

if n in a:
   print("yes")
else:
   print("no")
