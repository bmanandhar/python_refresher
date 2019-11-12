#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:02:18 2019

@author: bijayamanandhar
"""
class Solution:
    
    def reverse_string(self, text):
        
        result = ''
        
        array = [None] * len(text)
                
        for i in range(len(text)):
            array[i] = text[len(text) - 1 - i]
        
        result = ''.join(array)
        
        return result
    
if __name__== '__main__':
    text = "1-AbCdEfGh-9"
    S = Solution()
    print(S.reverse_string(text) == "9-hGfEdCbA-1") #Should print True
    print(S.reverse_string(".gnirts desrever a saw tI")) #Should print "It was a reversed string."



