#!/usr/bin/env python3

s = input()
while s != "end":
   token = " ".join(s.split())
   if token[0] == "3":
      print(token[:])
   s = input()
