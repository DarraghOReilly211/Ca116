#!/usr/bin/env python3

n = input()
n = n.split(" ")
#print(n[0], n[1], n[2])
dictionary = {}
a = []


i = 0
while i != 1:
   if int(n[0]) < int(n[1]) and int(n[0]) < int(n[2]):
      dictionary["A"] = int(n[0])
      i = 1
   elif int(n[1]) < int(n[0]) and int(n[1]) < int(n[2]):
      dictionary["A"] = int(n[1])
      i = 1
   else:
      dictionary["A"] = int(n[2])
      i = 1

i = 0
while i != 1:
   if int(n[0]) > int(n[1]) and int(n[0]) > int(n[2]):
      dictionary["C"] = int(n[0])
      i = 1
   elif int(n[1]) > int(n[0]) and int(n[1]) > int(n[2]):
      dictionary["C"]  = int(n[1])
      i = 1
   else:
      dictionary["C"] = int(n[2])
      i = 1

#print(dictionary)
i = 0
while i != 1:
   if int(n[0]) < dictionary["C"] and dictionary["A"] < int(n[0]):
      dictionary["B"] = int(n[0])
      i = 1
   elif int(n[1]) < dictionary["C"] and dictionary["A"] < int(n[1]):
      dictionary["B"] = int(n[1])
      i = 1
   else:
      dictionary["B"] = int(n[2])
      i = 1

#print(dictionary)
s = str(input())

i = 0
while i < len(s):
   #print(dictionary[s[i]])
   a.append(str(dictionary[s[i]]))
   i = i + 1

a = " ".join(a)
print(a)
