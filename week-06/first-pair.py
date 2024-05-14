#!/usr/bin/env python3

s = (input())
i = 1
j = 0

while i < len(s) and not (s[i] == s[i - 1]):
   i = i + 1
if i < len(s):
   j = i
   while j < len(s) and s[j] == s[j - 1]:
      j = j + 1
   print(s[i - 1:j])
