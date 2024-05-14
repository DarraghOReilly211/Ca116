#!/usr/bin/env python3

n = 10
i = 0
s = int(input())

while (i < n - 1):
   x = int(input())
   if x > 0 and x > s:
      x = s
   i = i + 1
print(x)
