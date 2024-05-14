#!/usr/bin/env python3

m = int(input())
i = 0
while i < 9:
   x = int(input())
   if x < m and x > 0:
      m = x
   i = i + 1
print(m)
