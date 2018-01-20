#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
sosq=0
sqos=0
n, m=1, 1
y=0
a=int(input("Enter a number: "))
while n<=a:
    x=(n)**2
    sosq+=x
    n+=1
print(sosq)
while m<=a:
    y=y+m
    m+=1
    sqos=y**2
print(sqos)
diff= sqos-sosq
print("The answer is: ", diff)
    