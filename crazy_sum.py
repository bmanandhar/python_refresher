#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:15:58 2019

@author: bijayamanandhar
"""

"""
Write a function crazy_sum(array) that adds all the integers
in the given array multiplied with the respective indices.
For example: total of [2, 6, -1] is 2*0 + 6*1 + (-1)*2 = 4.
0, 1 and 2 are the indices of 2, 6, and -1 respectively.
"""

class Solution(object):
    
    def crazy_sum(self, array):
        
        total = 0
        for i in range(len(array)):
            
            total += array[i]*i
            
        return total
        
if __name__=="__main__":
    
    S = Solution()

    examples = [
            [1, 3, 9],
            [5, -2, 7],
            [2, 0, 6, 3],
            [8, -1, 0, 3]
            ]    
    
    for example in examples:
        print(S.crazy_sum(example))


#End of file
