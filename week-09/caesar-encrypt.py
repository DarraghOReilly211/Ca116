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

s = "".join(sys.stdin.readlines())
s = "".join(s.strip())

i = 0
while i < len(s):
   if s[i] in translation:
      a.append("".join((translation[s[i]])))
   else:
      a.append(s[i])
   i = i + 1

a = "".join(a)
print(a)
