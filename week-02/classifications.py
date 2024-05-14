#!/usr/bin/env python3

n = int(input())

print("first" + ":", (n >= 70))
print("second" + ":", (50 <= n <= 69))
print("third" + ":", (40 <= n <= 49))
print("fail" + ":", (n < 40))
