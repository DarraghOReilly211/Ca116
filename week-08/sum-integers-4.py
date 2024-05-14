#!/usr/bin/env python3

import sys
files = sys.argv[1:]

total = 0
i = 0
j = 0
k = 0
n = 0
while i < len(files):
   with open(files[i]) as f:
      j = 0
      while j < len(files[i]):
         lines = f.readline()
         lines = (lines.split(" "))
         n = 0
         k = 0
         while n < len(lines):
            if lines[k] != "":
               total = total + int(lines[k])
               k = k + 1
               n = n + 1
            else:
               n = len(lines)
         j = j + 1
   i = i + 1

print(total)
