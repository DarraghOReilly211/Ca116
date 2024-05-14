#!/usr/bin/env python3

import sys

file1 = "a.txt"
file2 = "b.txt"
dic = {}
key = ""
check = "disjoint"

with open(file1, "r") as f:
    key = f.readline().strip()
    while 0 < len(key):
        if key not in dic:
            dic[key] = key
        key = f.readline().strip()

with open(file2, "r") as f:
    key = f.readline().strip()
    while 0 < len(key):
        if key in dic:
            check = "intersecting"
        key = f.readline().strip()

print(check)
