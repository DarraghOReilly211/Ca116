#!/usr/bin/env python3

x = str(input())
w = str(input())
y = str(input())

a = len(x)
b = len(w)
c = len(y)
if (a > b) and (a > c):
   print(x)
elif (b > a) and (b > c):
   print(w)
else:
   print(y)
