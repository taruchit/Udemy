# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:03:13 2021

@author: pc
"""
import math

#Input
n=int(input())

print("User input: ",n)

count1=0
count2=0

print("Brute force approach: -")
#Time complexity: O{n)
prime=-1
for i in range(2,n):
    count1=count1+1
    if(n%i==0):
        print(n," is not a prime number")
        prime=1
        break
if(prime==-1):
    print(n," is a prime number")

print("Better approach: -")
'''
Let 'n' be a non prime number
n = a * b
a belongs to range 2 to (n-a)

Let us assume 'a' be the smaller number compared to 'b'.

=> a * b >= a * a
=> n >= a * a
=> a <= sqrt(a)


'''
#Time complexity: O(sqrt(n))
prime=-1
limit=int(math.sqrt(n))
for i in range(2,limit+1):
    count2=count2+1
    if(n%i==0):
        print(n," is not a prime number")
        prime=1
        break
if(prime==-1):
    print(n, " is a prime number")
    
    
print("Number of for loop iterations in Brute force approach: ",count1)
print("Number of for loop iterations in Better approach: ",count2)    
