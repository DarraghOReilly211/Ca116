#!/usr/bin/env python3

curr = int(input())
if curr != 0:
   past = curr
   curr = int(input())
while curr != 0:
   if curr > past:
      print("higher")
      past = curr
   elif (curr == past):
      print("equal")
   else:
      print("lower")
      past = curr
   curr = int(input())
