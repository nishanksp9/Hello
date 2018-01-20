#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
#q=2
#count=0
n=int(input("Enter a number:"))
for i in range (2, n+1, 1):
    count=0
    if n%i==0:
        #print(i)
        for q in range (2, i+1, 1):
            if i%q==0:
                count+=1
        if count==1:
            print(i)
                
        
            
            