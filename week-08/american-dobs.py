#!/usr/bin/env python3

import sys

input_f = "irish-dobs.txt"
output_f = "american-dobs.txt"

i = 0
with open(output_f, "w") as f_out:
    with open(input_f, "r") as f:
        line = f.readline()
        while 0 < len(line):
            words = line.split(" ")
            date = words[0]
            dates = date.split("/")

            name = " ".join(words[1:])

            am_date = dates[1] + "/" + dates[0] + "/" + dates[2]

            i = i + 1
            f_out.write(am_date + " " + name)
            line = f.readline()
