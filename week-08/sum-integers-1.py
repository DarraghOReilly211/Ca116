#!/usr/bin/env python3

import sys

total = 0
s = sys.stdin.readline()

while 0 < len(s):
   total = total + int(s)
   s = sys.stdin.readline()

print(total)
