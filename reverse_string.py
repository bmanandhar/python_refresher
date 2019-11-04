#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:02:18 2019

@author: bijayamanandhar
"""
class Solution(object):
    
    def reverse_string(text):
        result = ''
        
        array = [None] * len(text)
        
        text = list(text)
        
        for i in range(len(text)):
            array[i] = text[len(text) - 1 - i]
        
        result = ''.join(array)
        
        return result
    
if __name__== '__main__':
    text = "1-AbCdEfGh-9"
print(reverse_string(text))

