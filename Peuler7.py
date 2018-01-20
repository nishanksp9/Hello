#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:02:24 2018

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
i=1
count=0
c=int(input("In the series of prime numbers, which term do you want?"))
while count<=c-1:
    k=0
    for j in range (1, i+1 , 1):
        if i%j==0:
            k+=1
    if k==2:
        count+=1
        #print(i)
    i+=1
print("Prime number #"+ str(c) +" is: ", i-1)