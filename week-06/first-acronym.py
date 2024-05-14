#!/usr/bin/env python3

s = (input())
i = 0
j = len(s)
k = 0

while i != j:
   if "a" <= s[i] <= "z" or s[i] == " ":
      i = i + 1
   else:
      j = i

j = j + 1
while j <= len(s):
   if j == len(s):
      print(s, i)
      j = j + 1
   elif "a" <= s[j] <= "z" or s[j] == " " or s[j] == ",":
      k = j
      j = len(s) + 1
      print(s[i:k], i)
   else:
      j = j + 1
