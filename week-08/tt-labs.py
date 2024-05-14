#!/usr/bin/env python3

a = []
s = input()

while s != "end":
   a.append(s)
   s = input()

#print(a)

i = 0
while i != len(a):
   s = a[i]
   #print(s)
   if int(s[5]) > 1:
      print(s)
      i = i + 1
   else:
      i = i + 1
