#!/usr/bin/env python3

import sys
s = sys.argv[1]

i = 0
while i < len(s) and s[i] != "=":
   i = i + 1

field = s[:i]
value = s[i + 1:]

s = input()
position = 0
start = 0

end = 0
while end < len(s) and s[end] != ",":
   end = end + 1

while s[start:end] != field:
   position = position + 1
   start = end + 1

   end = start + 1
   while end < len(s) and s[end] != ",":
      end = end + 1

s = input()
while s != "end":
   start = 0

   i = 0
   while i < position:
      while start < len(s) and s[start] != ",":
         start = start + 1

      start = start + 1
      i = i + 1

   end = start + 1
   while end < len(s) and s[end] != ",":
      end = end + 1

   if s[start:end] == value:
      print(s)

   s = input()
