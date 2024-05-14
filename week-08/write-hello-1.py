#!/usr/bin/env python3

import sys
args = sys.argv[1:]
total = 0

message = "Hello world."
file_name = "hello.txt"

with open(file_name, "w") as f:
   line = f.readline()
   total = total + int(line)
