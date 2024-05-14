#!/usr/bin/env python3

a = []
s = input()
n = 0
while s != "end":
   token = s.split()
   n = n + int(token[2])
   s = input()

print(n)
