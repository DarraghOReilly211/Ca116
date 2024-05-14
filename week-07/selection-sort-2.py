#!/usr/bin/env python3

i = 0
j = 0
a = []
s = input()

while s != "end":
   a.append(int(s))
   s = input()

n = int(input())
i = n
while i < len(a):
   if a[i] < a[j]:
      j = i
   i = i + 1
print(j)
