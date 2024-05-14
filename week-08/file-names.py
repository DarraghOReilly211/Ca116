#!/usr/bin/env python3

import sys

s = sys.stdin.readline()
i = 0
while i < len(s):
    s = s.split("/")
    p = s[len(s) - 1]
    sys.stdout.write(p)
    s = sys.stdin.readline()
