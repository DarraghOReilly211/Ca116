#!/usr/bin/env python3
 
import sys 
snap = {}
#print(seen)
s = sys.stdin.readline().strip()
while 0 < len(s) and s not in snap:
   snap[s] = True
   s = sys.stdin.readline().strip()
if s in snap:
   print("snap: " + s)