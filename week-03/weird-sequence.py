#!/usr/bin/env python3

i = 0
x = 0
n = int(input())
print(x)
while i < (n - 1):
   x = ((-x) - ((-1) ** (x % 2)))
   print(x)
   i = i + 1
