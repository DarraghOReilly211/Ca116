#!/usr/bin/env python3

s = input()
a = []
for i in s:
    if i == "<" and len(a) > 0:
        a.pop()
    else:
        a.append(i)
print("".join(a))