#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:26:47 2019

@author: bijayamanandhar
"""

'''
write a function, bubble_sort(arr), 
that acts to sort an array in a bubble methodology.
'''

class Solution(object):
    
    def bubble_sort(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
        
    
if __name__ == '__main__':
    
    S = Solution()
    
    arrays = [
            [2, 9, 1, 5, 7],
            [-2, 5, 0, 8, 10],
            [90, -8, 0, 34, 74, -8]
            ]
    
    for i in range(len(arrays)):
        print(S.bubble_sort(arrays[i]))