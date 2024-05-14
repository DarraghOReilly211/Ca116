#!/usr/bin/env python3

j = 1
p = 0
a = []
s = input()

while s != "end":
   a.append(int(s))
   s = input()


while j < len(a):
   if a[j] < a[p]:
      p = j
   j = j + 1
print(p)
