#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:36:23 2019

@author: bijayamanandhar
"""

'''
Odd-man Out...
You are given an array of integers where every element appears twice,
except for one integer which appears only once. 
Write an algorithm that finds the element which appears only once. 
'''

class Solution:
    
    def oddManOut(self, array):

        dict = {}
        for i in array:
            
            if i not in dict:
                
                dict[i] = 1
            else:
                dict[i] += 1
        for key in dict:
            
            if dict[key] == 1:
            
                return key
        return False
                              
if __name__ == '__main__':
    
    S = Solution()
    
    examples = [
            [3, 1, 1, 3],
            [9, -8, 9, 10, -8, 1, 1],
            [13, 71, 68, 68, 13],
            [30, 60, 60, -19, 30]
            ]
    
    for example in examples:
        print(S.oddManOut(example))
        
        
        #End
       
       
        
        