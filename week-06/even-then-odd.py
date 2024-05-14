#!/usr/bin/env python3

test_list = []
a = []
b = []
s = str(input())
while s != "end":
   test_list.append(s)
   s = str(input())
i = 0
while i < len(test_list):
   if i < len(test_list) and int(test_list[i]) % 2 == 0:
      test_list[i] = int(test_list[i])
      a.append(test_list[i])
      i = i + 1

   else:
      test_list[i] = int(test_list[i])
      b.append(test_list[i])
      i = i + 1
i = 0
while i < len(a):
   print(a[i])
   i = i + 1

i = 0
while i < len(b):
   print(b[i])
   i = i + 1
