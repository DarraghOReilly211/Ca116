#!/usr/bin/env python3

a = int(input())
b = int(input())

if a % 2 == 1 and b == ((a * 3) + 1):
   print("yes")
elif a % 2 == 0 and a // 2 == b:
   print("yes")
else:
   print("no")
