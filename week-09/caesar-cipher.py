#!/usr/bin/env python3

import sys
normal = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
caesar = " nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
translation = {}
a = []
i = 0
while i < len(normal):
   translation[normal[i]] = [caesar[i]]
   i = i + 1
#print(translation)

s = sys.stdin.readline().strip()
i = 0
#print(s)
while i < len(s):
   if s[i] in normal:
      a.append(" ".join(translation[s[i]]))
   i = i + 1

a = "".join(a)
print(a)