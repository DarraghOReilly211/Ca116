#!/usr/bin/env python3

import sys

t = sys.argv[1]
s = input()

# Find the position of the start of the nth field.
start = 0
pos = 0
i = 0
j = len(t)
end = 0


while i < len(s):
    while start < len(s) and s[start] != ",":
        start = start + 1
    if s[pos:start] == t:
        print(i)
    pos = start + 1  # Jump over the comma.
    start = start + 1
    i = i + 1
