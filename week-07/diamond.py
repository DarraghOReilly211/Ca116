#!/usr/bin/env python3

import sys
args = sys.argv[1:]
a = int(args[0])
m = a // 2

i = 0
while i < m:
   print((" " * (m - i)) + ("*" * ((i * 2) + 1)))
   i = i + 1

i = 0
while i <= m:
   print((" " * i) + ("*" * (a - (2 * i))))
   i = i + 1
