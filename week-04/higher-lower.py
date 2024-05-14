#!/usr/bin/env python3

past = int(input())
i = 0
while i < 5:
   curr = int(input())
   if curr > past:
      print("higher")
      past = curr
   elif (curr == past):
      print("equal")
   else:
      print("lower")
      past = curr
   i = i + 1
