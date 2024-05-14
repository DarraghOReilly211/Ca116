#!/usr/bin/env python3

x = int(input())
y = (x % 100)
x = (x - y)
x = (x // 100)
x = (x % 100)
print(x)
