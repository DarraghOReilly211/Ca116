#!/usr/bin/env python3

x = int(input())
z = (x // 100)
m = (z // 100)
d = (z % 100)
d = (d * 10000)
m = (m * 100)
x = (x % 100)
date = (d + m + x)
print(date)
