#!/usr/bin/env python3

i = 1
while i != 0:
   n = int(input())
   if (n % 3 == 0 and n % 5 == 0):
      i = 0
   else:
      i = i + 1
print(n)
