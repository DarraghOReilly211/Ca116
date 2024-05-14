#!/usr/bin/env python3

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11]

i = 0
tmp = 0


while i < 1:
   tmp = a[i]
   a[i] = a[len(a) - 1]
   a[len(a) - 1] = tmp
   i = i + 1
