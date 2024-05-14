#!/usr/bin/env python3

x = int(input())
i = 0
n = 10

while i < (n - 1):
   s = int(input())
   if x < s:
      x = s
   i = i + 1
print(x)
