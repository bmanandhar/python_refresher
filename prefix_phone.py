#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:22:11 2019

@author: bijayamanandhar
"""

"""
Given:
    
-A list of prefixes for discount on phone calls
-A list of phone numbers
-Select the prefix phones and form a list as result     
"""

class Solution:
    
    def prefix_phone(self, prefixes, numbers):
        
        selected = []
        
        for prefix in prefixes:
            
            for number in numbers:
                
                if number[:len(prefix)] == prefix:
                    selected.append(number)
                    
        return selected
    
    
if __name__ == '__main__':
    
    S = Solution()
    
    prefixes = ['+1234', '+5678', '+3215', '+987']

    numbers = [
            '+9872349871',
            '+9871234665432',
            '+8712345671', 
            '+32159865342', 
            '45452677721',
            '+5678111222333', 
            '+8362412300',
            '+82726241611'
            ]    

    expected = [
            '+5678111222333',
            '+32159865342', 
            '+9872349871',
            '+9871234665432'
            ]
    
    print(S.prefix_phone(prefixes, numbers) == expected) #should print True
      
    
    
    