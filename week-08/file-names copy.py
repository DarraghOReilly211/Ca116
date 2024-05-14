#!/usr/bin/env python3

a = []
s = input()
while len(s) != 0:
   a.append(s)
   s = input()


a = " ".join(a)
a = a.split("/")
a = " ".join(a)
a = a.split(" ")
a = " ".join(a)
a = a.split("/")
a = " ".join(a)
a = a.split(" ")
a = " ".join(a)

i = 0
while i < (len(a) - 1):
   if (a[i][len(a[i]) - 6:]) == ".ascii":
      print(a[i])
      i = i + 1
   elif a[i] == a[i - 1] and len(a[i]) != 0 and not a[i] == a[i - 2]:
      i = i + 1
   elif (a[i][len(a[i]) - 3:]) == ".py":
      print(a[i])
      i = i + 1
   else:
      i = i + 1
