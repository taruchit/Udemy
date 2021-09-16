# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:55:15 2021

@author: pc
"""
print("Case 1: -")

#Taking the input
a=int(input())
b=int(input())

#Swaping the data between two variables by taking a  temporary variable
temp=a
a=b
b=temp

#Output
print("a : ",a)
print("b : ",b)

print("Case 2: -")

#Taking the input
a=int(input())
b=int(input())

#Swaping the data without temporary variables
a,b=b,a

#Output
print("a : ",a)
print("b : ",b)