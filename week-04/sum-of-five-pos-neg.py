#!/usr/bin/env python3

pos = 0
neg = 0
n = int(input())
i = 0

while i < 5:
   if n < 0:
      neg = neg + n
      i = i + 1
   else:
      pos = pos + n
      i = i + 1
   n = int(input())

print(neg, pos)
