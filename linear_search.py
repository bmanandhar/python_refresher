#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:10:41 2019

@author: bijayamanandhar
"""

class Solution:
    
    def linear_search(self, list, n):
        
        global i
        i = 0
        
        while i < len(list):
            
            if list[i] == n:
                return True
            
            i += 1
        return False
        
        
if __name__ == "__main__":
    
    S = Solution()
    
    examples = (
            ([2, 1, 4, 9, 0], 4),
            ([-6, 6, 19, 10, 8], 10),
            ([3, 9, 5, 7, 8], 6),
            ([4, 9, 1, 8, 11], 11)
            )
    
    for example in examples:
        
        if S.linear_search(example[0], example[1]):
            print("Found at index:", i)
        print("Not found")
        
        
    
    
    
    
    
    
    
    