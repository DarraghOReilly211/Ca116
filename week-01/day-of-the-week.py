#!/usr/bin/env python3

month = int(input())
day = int(input())

day = day - 1
month = ((month - 1) * 30)

print(((day + month) % 7) + 1)