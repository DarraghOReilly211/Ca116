#!/usr/bin/env python3

s = input()
while s != "end":
   token = " ".join(s.split()[5:])
   print(token)
   s = input()
