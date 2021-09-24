# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:01:27 2021

@author: pc
"""

def buildPartialSumArray(a,s,T):
    s.append(a[0])
    for i in range(1,T):
        print("i : ",i)
        print("i-1 : ",i-1)
        temp=s[i-1]+a[i]
        print("temp: ",temp)
        s.append(temp)
    return s
    
#Number of inputs from the user
T=int(input())

#Creating a list
a=list()

#Taking user inputs for the array
for i in range(T):
    a.append(int(input()))
    
#Printing the array
print(a)

#Creating the partial sum array
s=list()

#Building Partial Sum array
s=buildPartialSumArray(a, s, T)

#Printing partial sum array
print(s)

#Taking user input for bouandry values: x and y
print("Enter value of x: -")
x=int(input())
print("Enter value of y: -")
y=int(input())

#Computing partial sum
a=s[y]
b=s[x-1]
print("s[y]: ",a)
print("s[x-1]: ",b)
res=a-b

#Printing the result
print("Result:  ",res)