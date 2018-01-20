#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 04:36:13 2018

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
a=0
b=0
c=0
for a in range(0, 500, 1): #as a, b, c are pythagorean triplets & a+b+c=1000
    for b in range(a+1, 500, 1): # the individual values of a & b will be < 500
        c=1000-a-b
        if (a<b<c):
            if (a**2 + b**2 == c**2):
                print(a,b,c, a*b*c)