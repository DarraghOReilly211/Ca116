#!/usr/bin/env python3

s = (input())
p = ""

if s[0] == "-":
   p = "-"
   s = s[1:]

i = 0
while i < len(s) and s[i] != ".":
   i = i + 1

if i < len(s):
   integer = s[:i]
   fraction = s[i + 1:]
else:
   integer = s
   fraction = ""

if len(integer) == 0:
   integer = "0"

if len(fraction) == 0:
   fraction = "0"

print(p + integer + "." + fraction)
