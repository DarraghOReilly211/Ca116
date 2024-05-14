#!/usr/bin/env python3

import sys
ppm = sys.stdin.readline().split()

t1 = sys.stdin.readline().split()
t2 = sys.stdin.readline().split()
t3 =sys.stdin.readline().split()

#Find last to arrive
i = 0
while i != 1:
   if  int(t2[0]) < int(t1[0]) and int(t3[0]) < int(t1[0]):
      highest_arrival = int(t1[0])
      i = 1
   elif int(t1[0]) < int(t2[0]) and int(t3[0]) < int(t2[0]):
      highest_arrival = int(t2[0])
      i = 1
   else:
      highest_arrival = int(t3[0])
      i = 1

i = 0 
while i != 0:
   if  int(t1[1]) < int(t2[1]) and int(t1[1]) < int(t3[1]):
      lowest_departure = int(t1[1])
      i = 1
   elif int(t2[1]) < int(t1[1]) and int(t2[1]) < int(t3[1]):
      lowest_departure = int(t2[1])
      i = 1
   else:
      lowest_departure = int(t3[1])
      i = 1

total = 0
total = total + ((lowest_departure - highest_arrival) * ppm[2])

i = 0
while i != 0:
   if int(t1[0]) < int(t2[0]) and int(t1[0]) < int(t3[0]):
      lowest_arrival = int(t1[0])
      i = 1
   elif int(t2[0]) < int(t1[0]) and int(t2[0]) < int(t3[0]):
      lowest_arrival = int(t2[0])
      i =1
   elif int(t3[0]) < int(t1[0]) and int(t3[0]) < int(t2[0]):
      lowest_arrival = int(t3[0])
      i = 1

i = 0
while i != 0:
   if int(t1[1]) > int(t2[1]) and int(t1[1]) > int(t3[1]):
      highest_departure = int(t1[1])
      i = 1
   elif int(t2[1]) > int(t1[1]) and int(t2[1]) > int(t3[1]):
      highest_departure = int(t2[1])
      i =1
   elif int(t3[1]) > int(t1[1]) and int(t3[1]) > int(t2[1]):
      highest_departure = int(t3[1])
      i = 1

i = 0 
while i != 1:
   if int(t1[0]) < highest_arrival and int(t1[0]) > lowest_arrival:
      middle_arrival = int(t1[0])
   elif int(t2[0]) < highest_arrival and int(t2[0]) > lowest_arrival:
      middle_arrival = int(t2[0])
   else:
      middle_arrival = int(t3[0])

i = 0 
while i != 1:
   if int(t1[1]) < highest_departure and int(t1[1]) > lowest_departure:
      middle_departure = int(t1[0])
   elif int(t2[1]) < highest_departure and int(t2[1]) > lowest_departure:
      middle_departure = int(t2[0])
   else:
      middle_departure = int(t3[0])

total = total + ((middle_departure - middle_arrival) * ppm[1])

