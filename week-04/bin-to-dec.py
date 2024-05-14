#!/usr/bin/env python3

s = input()
dec = 0

i = 0
while i < len(s):
   d = (int(s[i]) * (2 ** (len(s) - i - 1)))
   dec = dec + d
   i = i + 1
print(dec)
