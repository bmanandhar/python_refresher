#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:01:48 2019

@author: bijayamanandhar
"""

'''
In the binary search method, all the elements have to be sorted.
This will work for an array with elements sorted in ascending order. 
'''

class Solution(object):
    
    def binary_search(self, array, num):
        
        low = 0
        high = len(array)-1
        global mid
        
        if num == array[0]: 
            mid = 0
            return True
        if num == array[len(array) - 1]:
            mid = len(array) - 1
            return True
        
        while low < high:
            
            
            mid = (low+high)//2
            
            if array[mid] == num:
                return True
            
            elif array[mid] < num:
                    low = mid+1
                
            else:
                high = mid+1
        
        return False

if __name__ == '__main__':
    
    S = Solution()
    
    examples = (  
            ([7, 8, 12, 34, 45, 99], 7),
            ([4, 7, 8, 12, 34, 45, 99], 45),
            ([1, 3, 5, 7, 11], 12),
            ([2, 9, 10, 11, 15], 15),
            ([4, 9, 23, 32, 56], 23),
            ([-8, -6, -5, -3, -1], -1)
            )
    
    for example in examples:    
        if S.binary_search(example[0], example[1]):
            
            print('Found at index:', mid)
        else: print('Not found!')
    
                    
