#!/usr/bin/env python3

n = int(input())

x = (n % 2)
if (x == 0):
  print(n // 2)
elif (x == 1):
  print((n * 3) + 1)
