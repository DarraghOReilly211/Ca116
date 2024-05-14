#!/usr/bin/env python3

s = str(input())
i = 0

if (s[i] == s[len(s) - i - 1]):
   while i < len(s) and (s[i] == s[len(s) - i - 1]):
      #print(s[i], s[len(s) - i - 1])
      i = i + 1
if i == len(s):
   print("palindrome")
