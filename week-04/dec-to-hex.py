#!/usr/bin/env python3

base = 16
h = "0123456789abcdef"
s = ""
n = int(input())
while 0 < n:
   d = n % base
   d = h[d]
   s = str(d) + s
   n = n // base
print(s)
