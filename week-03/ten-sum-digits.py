#!/usr/bin/env python3

n = 10
i = 0
total = 0

while i < n:
   w = int(input())
   if w > 0:
      total = total + (w % 10)
   else:
      total = total + ((-w) % 10)
   i = i + 1

print(total)
