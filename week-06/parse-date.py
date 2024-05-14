#!/usr/bin/env python3

s = input()
i = 0
j = 0
a = []
while i != len(s):
   if s[i] == " " or s[i] == ",":
      n = s[j:i]
      #print(n)
      a.append(n)
      j = i + 1
   i = i + 1
n = s[j:]
a.append(n)
#print(a[2])

day = "(" + a[0] + ")"
a[0] = a[2]
year = a[len(a) - 1]
a[2] = year
a[1] = a[1] + ","
a[len(a) - 1] = day

s = ""
i = 0
while i < len(a):
   if i == 0 or i == len(a) - 1:
      s = s + a[i]
   else:
      s = s + " " + a[i]
   i = i + 1

print(s)
