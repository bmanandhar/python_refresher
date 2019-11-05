#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:10:42 2019

@author: bijayamanandhar
"""
'''  
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which 
could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer 
overflows.
'''
class Solution:
    
    def reverse(self, x: int) -> int:
                
        x_str = str(abs(x))
        
        list = [None] * len(x_str)
        
        for i in range(len(x_str)):
            list[i] = x_str[len(x_str) - 1 - i]
            
        num_reversed = ''.join(list)
            
        if x < 0:
            num_reversed = '-' + num_reversed
            
        if int(num_reversed) < -2**31 or int(num_reversed) > 2**31-1:
            return 0
        
        return int(num_reversed)



if __name__ == '__main__':
    S = Solution()
    print(S.reverse(-1234))
    print(S.reverse(82309))
    print(S.reverse(9**9))
    print(S.reverse(-2**32))    #Extreme case, retuens 0
    print(S.reverse(2**32))     #Extreme case, returns 0
    print(S.reverse(-2**29))



    