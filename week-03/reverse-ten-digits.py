#!/usr/bin/env python3

t = 0
i = 0
n = 10
r = 10

while i < n:
   m = int(input())
   t = (t + m) * 10
   i = i + 1
t = t // 10

i = 0
while i < n:
   s = t % 10
   print(s)
   t = t // 10
   i = i + 1
