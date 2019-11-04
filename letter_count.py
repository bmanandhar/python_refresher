#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:05:16 2019

@author: bijayamanandhar
"""
'''
Write a function, `letter_count(str)` that takes a string 
and returns a hash mapping each letter to its frequency. 
Do not include spaces.
'''

class Solution(object):
    
    def letter_count(self, str):
        
        dict = {}
        
        for char in str:
            if char != ' ':
                if char not in dict:
                    dict[char] = 1
                else:
                    dict[char] += 1   
                    
        return dict
    
if __name__ == '__main__':
    
    strings = [
            'word', 
            'sentence', 
            'america', 
            'currency', 
            'fantastic', 
            'stations'
            ]
    
    S = Solution()
    
    for i in range(len(strings)):
        print(S.letter_count(strings[i]))
    
    