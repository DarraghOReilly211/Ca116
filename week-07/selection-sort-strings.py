#!/usr/bin/env python3

a = []
i = 0
j = 0

s = input()
while s != "end":
   a.append(s)
   s = input()

while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   i = i + 1

i = 0
while i < len(a):
   print(a[i])
   i = i + 1
