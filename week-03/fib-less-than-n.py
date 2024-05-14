#!/usr/bin/env python3

n = int(input())
i = 0
p = 1
c = 0

while i < n:
   print(c)
   p = (c + p)
   c = (p - c)
   i = c
