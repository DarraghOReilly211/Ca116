#!/usr/bin/env python3

import sys
args = sys.argv[1:]
args = "".join(args)
args = int(args)

i = 0
while (i ** 2) < args:
   print(i)
   i = i + 1
