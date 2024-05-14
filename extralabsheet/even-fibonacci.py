#!/usr/bin/env python3

import sys
args = sys.argv[1:]
args = args[0]
a = [1, 2]

i = 0
while i < 31:
   b = (int(a[(len(a) - 2)]) + int(a[len(a) - 1]))
   a.append(b)
   i = i + 1

n = 0
i = 0
while i < len(a):
   if int(a[i]) < int(args) and (int(a[i]) % 2) == 0:
      n = n + int(a[i])
      i = i + 1
   else:
      i = i + 1

print(n)
