#!/usr/bin/env python3

import sys

file1 = "a.txt"
file2 = "b.txt"
dic = {}
key = ""

with open(file1, "r") as f1:
    key = f1.readline().strip()
    while 0 < len(key):
        if key not in dic:
            dic[key] = key
        key = f1.readline().strip()

with open(file2, "r") as f:
    key = f.readline().strip()
    while 0 < len(key):
        if key in dic:
            print(dic[key])
        key = f.readline().strip()
