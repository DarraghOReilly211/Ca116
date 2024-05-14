#!/usr/bin/env python3

import sys

input_f = "input.txt"

with open(input_f, "r") as f:
    lines = f.readlines()
    lines = "".join(lines)
    sys.stdout.write(lines)
