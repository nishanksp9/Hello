#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
#n=int(input("Enter a number : " ))
#x=str(n)
#check=x
#recheck=x[::-1]
#if check==recheck:
#    print("The number is palindrome")
#else:
#    print ("The number is not a palindrome")
largest=0
for a in range (100,1000):
    for b in range (100,1000):
        pal=a*b
        x=str(pal)
        check=x
        recheck=x[::-1]
        if check==recheck:
            if largest>pal:
                print(largest)
                #print(a,b)
                break
            else:
                largest=pal
                #break
                print(a,b)
                break
        