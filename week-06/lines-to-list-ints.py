#!/usr/bin/env python3

test_list = []
s = str(input())
while s != "end":
   test_list.append(s)
   s = str(input())
i = 0
while i < len(test_list):
   test_list[i] = int(test_list[i])
   i = i + 1
print(test_list)
