#!/usr/bin/env python3

n = int(input())
i = 0
m = n // 2

while i <= m:
   if i < m:
      print((" " * i) + "*" + (" " * (n - (i * 2) - 2) + "*"))
   else:
      print((" " * m) + "*")
   i = i + 1
i = 0
while i < m:
   print(((" " * (m - i - 1)) + "*" + (" " * ((i * 2) + 1)) + "*"))
   i = i + 1
