#!/usr/bin/env python3

s = str(input())

i = 0
t = ""
while i < len(s):
    t = t + (s[len(s) - 1 - i])
    i = i + 1

print(t)
