#!/usr/bin/env python3

s = str(input())
n = int(input())

m = (s + "-") * n
print(m[0:(len(m) - 1)])
