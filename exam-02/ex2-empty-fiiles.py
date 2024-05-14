#!/usr/bin/env python3

import sys

args = sys.argv[1:]

args = args.split(" ")

a = []
i = 0
while i < args:
   with open(args[i]) as f:
      if len(f.readlines()) == 0:
         a.append(args[i] + "\n")
         i = i + 1
      else:
         i = i + 1

print(a)
