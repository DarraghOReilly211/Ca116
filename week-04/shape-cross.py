#!/usr/bin/env python3

n = int(input())
i = 0
m = n // 2
while i < n:
   if (i > m):
      print((" " * m) + "*")
   elif i == m:
      print("*" * n)
   else:
      print((" " * m) + "*")
   i = i + 1
