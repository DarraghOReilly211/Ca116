#!/usr/bin/env python3

import sys
german = "eins zwei drei vier funf sechs sieben acht neun zehn"
english = "one two three four five six seven eight nine ten"

german = german.split()
english = english.split()

i = 0
s = sys.stdin.readline().strip()
while 0 < len(s):
   if s == english[i]:
      print(german[i])
      i = 0
      s = sys.stdin.readline().strip()
   else:
      i = i + 1
