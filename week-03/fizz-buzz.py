#!/usr/bin/env python3

i = 1
n = int(input())

while(i < (n + 1)):
  if (((i % 3) == 0) and ((i % 5) == 0)):
      print("fizz-buzz")
  elif ((i % 3) == 0):
      print("fizz")
  elif ((i % 5) == 0):
      print("buzz")
  else:
      print(i)
  i = i + 1
