#!/usr/bin/env python3

import sys
args = sys.argv[1]

message = "Hello world."
file_name = sys.argv[1]

with open(file_name, "w") as f:
   f.write(message + "\n")
