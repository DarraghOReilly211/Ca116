#!/usr/bin/env python3

n = int(input())
s = int(input()) + 1

digit = (n % (10 ** s))
digit = (digit // (10 ** (s - 1)))
print(digit)
