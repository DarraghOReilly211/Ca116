#!/usr/bin/env python3

import sys

word = sys.stdin.readline().strip()
fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

while 0 < len(word):
   if word in fruit:
      print(word)
   word = sys.stdin.readline().strip()
