#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   j = 0
   while int(a[j]) > int(a[i]):
      if int(a[i]) < int(a[j]):
         tmp = a[j]
         a[j] = a[i]
         a[i] = tmp
      else:
         j = j + 1
   i = i + 1

a = "\n".join(a)
print(a)
