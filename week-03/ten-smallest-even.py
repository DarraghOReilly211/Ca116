#!/usr/bin/env python3

n = 10
i = 0
m = int(input())

while (i < n - 1):
   x = int(input())
   if (x % 2) == 0 and x < m:
      m = x
   i = i + 1
print(m)
