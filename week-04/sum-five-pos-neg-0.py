#!/usr/bin/env python3

n = int(input())
neg = 0
pos = 0
while n != 0:
   if n < 0:
      neg = neg + n
   else:
      pos = pos + n
   n = int(input())
print(neg, pos)
