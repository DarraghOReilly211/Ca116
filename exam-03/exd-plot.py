#!/usr/bin/env python3

import sys

n = sys.stdin.readlines()
n = "".join(n)
n = n.split("\n")
i = 0
points = []
while i < len(n):
   points.append(n[i])
   i = i + 1

#print(points)
i = 1
plot = "|"
while i != int(n[0]) + 1:
   d = (i - 1)
   if str(d) in points:
      plot = (plot + "*")
   else:
      plot = (plot + " ")
   i = i + 1
plot = plot + "|"
print(plot)
