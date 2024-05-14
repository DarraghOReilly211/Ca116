#!/usr/bin/env python3

n = 10
i = 0
s = int(input())

while i < (n - 1):
   r = int(input())
   if r < s:
      s = r
   i = i + 1
print(s)
