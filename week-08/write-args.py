#!/usr/bin/env python3

import sys
args = sys.argv[1]

s = " ".join(sys.argv[2:])
s = s.split(" ")

message = "s"
file_name = sys.argv[1]

i = 0
with open(file_name, "w") as f:
   while i < len(s):
      f.write(s[i] + "\n")
      i = i + 1
