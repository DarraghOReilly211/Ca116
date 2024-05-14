#!/usr/bin/env python3

s = str(input())

while s != "end":
   token = s.split()
   start = token[1]
   start = int(start)
   duration = token[2]
   end = ((start + int(duration) - 1) % 24)
   start = str(start) + ":00"
   end = str(end) + ":50"
   token[1] = start
   token[2] = str(end)
   token = (" ".join(token))
   print(token)
   s = input()
