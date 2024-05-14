#!/usr/bin/env python3

n = int(input())
n = (n % 10000)
y = (n % 100)
n = (n - y)
n = (n // 100)
w = (n % 10)
z = ((n - w) // 10)

print((w * 10) + z)
