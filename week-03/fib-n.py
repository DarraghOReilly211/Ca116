#!/usr/bin/env python3

i = 0
c = 0
n = int(input())
p = 1

while (i < n):
   print(c)
   p = (c + p)
   c = (p - c)
   i = i + 1
