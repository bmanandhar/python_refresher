#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:20:19 2019

@author: bijayamanandhar
"""
'''
Given an array of integers, 
return indices of the two numbers
 such that they add up to a specific target.

You may assume that each input
would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [None] * 2
        
        for i in range(len(nums)-1):
            
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result[0], result[1] = i, j
                    
        return result
    
if __name__ == '__main__':
    S = Solution()
    
    examples = (
            ([1, 3, -6, 7], 1),
            ([0, 5, 9, 3], 8),
            ([8, 2, 7, 10, -2], 0),
            ([1, 2, 3, 4, 5, 6], 10),
            ([-9, 11, 8, 2, 1], -8)
            )
    
    for example in examples:
        
        print(S.twoSum(example[0], example[1]))
    
    
    
    
    