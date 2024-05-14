#!/usr/bin/env python3

x = int(input())
print(x // 100)
x = (x - ((x // 100) * 100))
print(x // 10)
print(x % 10)
