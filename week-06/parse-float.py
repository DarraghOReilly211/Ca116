#!/usr/bin/env python3

s = input()
i = 0

while s[i] != ".":
    i = i + 1
print(s[0:i])
j = i
while j <= len(s) and not s[j] == ".":
    i = i + 1
print(s[j + 1:])
