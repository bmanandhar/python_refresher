#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:39:33 2019

@author: bijayamanandhar
"""
class Solution(object):

    def palindrome(self, string):
        
        i = 0
        while i < len(string):
            if string[i] != string[(len(string) - 1) - i]:
                return False
            i += 1
        return True
    
if __name__ == '__main__':
    string = ['rotator', 'repaper', 'kayak', 'sagas', 'malayalam']
    
    S = Solution()
    
    for i in range(len(string)):
        
        print(S.palindrome(string[i])) # Prints 'True'
        
    
    