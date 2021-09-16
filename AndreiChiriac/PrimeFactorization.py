# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:18:55 2021

@author: pc
"""

#Taking the input
n=int(input())
print("n : ",n)

#Declaring two lists to store prime numbers and their power
fact=list()
power=list()

#Prime number
d=2


while(n>1):
    k=0
    while(n%d==0):
        n=n/d
        k=k+1
    if(k>0):
        fact.append(d)
        power.append(k)
    d=d+1
    
#Output
print("Prime factors: ",fact)
print("Power: ",power)