#!/usr/bin/env python3

import sys
seen = {}
s = sys.stdin.readline().strip()
while 0 < len(s):
   if s not in seen:
      seen[s] = True
   elif s in seen:
      seen[s] = False
   s = sys.stdin.readline().strip()

# seen = {
# 'dog':True - only one instance
# 'cat':False - more than one instance
# 'horse':False
# }
for s in seen:
   if seen[s]: #seen[s] = true or false
      print(s)
