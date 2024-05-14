#!/usr/bin/env python3

x = int(input())

if (x == 2) or (x == 3):
   print("prime")
elif (x % 2 == 0 or (x % 3 == 0) or x == 1):
   print("not prime")
else:
   print("prime")
