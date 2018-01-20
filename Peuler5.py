#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
"""
i=1
n=int(input("Enter a number: "))
for j in range (1, n+1, 1):
    if i%j>0:
        #print(i,j)
        for k in range (1, n+1):
            #print(i,j,k)
            if (i*k)%j==0:
                print(i,j,k)
                i=i*k
                break
print("The answer is: ", i)