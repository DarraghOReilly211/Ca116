#!/usr/bin/env python3

a = int(input())
b = int(input())

while b != 0:
   r = b
   b = a % b
   a = r
print(a)
