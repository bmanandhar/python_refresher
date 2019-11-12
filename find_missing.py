#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:40:26 2019

@author: bijayamanandhar
"""
def missing(arr):
    
    for i in range(len(arr) -1):
        
        if i > 0:
            left = arr[i] - arr[i -1]
            right = arr[i +1] - arr[i]
            
            if left != right:
                return (arr[i] + arr[i + 1])/2
                
print(missing([1, 2, 3, 4, 6, 7, 8, 9]) == 5)
print(missing([9, 7, 5, 3, -1, -3]) == 1)
print(missing([10, 15, 25, 50, 35]) == 20)
print(missing([0, -3, -6, -12, -15, -18]) == -9)



 