#!/usr/bin/env python3

a = []
b = []
s = input()

while s != "end":
   a.append(s)
   s = input()

#print(a)

j = 0
i = 0
while j < 10:
   while i < len(a):
      if int(a[i]) == j:
         b.append(a[i])
         i = i + 1
      else:
         i = i + 1
   print(j, "*" * len(b))
   b = []
   i = 0
   j = j + 1
