# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:58:52 2021

@author: pc
"""
#Input
x=int(input())
y=int(input())
p=int(input())

#Brute force approach
count=0
t=1
for i in range(y):
   t=t*x
   count=count+1
   
ans=t%p
print("Answer: ",ans)
print("Number of steps in for loop taken during Brute Force approach: - ",count)

#Using pow() method
ans=pow(x,y)%p
print("Answer: ",ans)



