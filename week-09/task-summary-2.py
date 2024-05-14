#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()
#print(s)
dick = {

}
i = 0
lenght = s
while i < len(lenght):
   d = s[i].split("/")
   d = " ".join(d)
   d = d.split(".")
   d = " ".join(d)
   d = d.split(" ")
   #print(d)
   if d[0] not in dick and d[len(d) - 1] == "incorrect\n":
      dick[d[0]] = 0

   elif d[0] not in dick and d[len(d) - 1] == "correct\n":
      dick[d[0]] = 1
   
   elif d[0] in dick and d[len(d) - 1] == "correct\n":
      dick[d[0]] = dick[d[0]] + 1
   
   elif d[0] in dick and d[len(d) - 1] == "incorrect\n":
      dick[d[0]] = dick[d[0]] - 1
   i = i + 1
#print(dick)
for d in dick:
   print(d, dick[d])
