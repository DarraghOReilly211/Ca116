#!/usr/bin/env python3

import sys

n = 20
points = {}

s = sys.stdin.readline()
while 0 < len(s):
    tokens = s.split()
    key = tokens[0] + "/" + tokens[1]
    points[key] = True
    #print(tokens)
    s = sys.stdin.readline()

print(" " + n * "-")

y = 0
i = 0
while i < n:
    y = n - i - 1
    a = []
    x = 0
    while x < n:
        key = str(x) + "/" + str(y)
        if key in points:
            a.append("*")
        else:
            a.append(" ")
        x = x + 1
    print("|" + "".join(a) + "|")
    i = i + 1

print(" " + n * "-")
