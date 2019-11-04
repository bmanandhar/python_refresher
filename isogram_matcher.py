#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:41:14 2019

@author: bijayamanandhar
"""

# Isogram Matcher
# ------------------------------------------------------------------------------
# An isogram is a word with only unique, non-repeating letters. Given two isograms
# of the same length, return an array with two numbers indicating matches:
# the first number is the number of letters matched in both words at the same position,
# and the second is the number of letters matched in both words but not in the
# same position.


class Solution(object):
    
    def isogram_matcher(self, word1, word2):
        
        x, y = 0, 0
    
        for i in range(len(word1)):
    
            for j in range(len(word1)):
                if word1[i] == word2[j]: 
                    
                    if i == j: 
                        x += 1 # matching both chars and indices
                    else:
                        y += 1 # matching chars but not indices
                        
        return [x, y]
    
if __name__ == "__main__":
    
    S = Solution()
    
    examples = [
            ["ultrasonic", "ostracized"],
            ["cat", "car"],
            ["england", "denmark"],            
            ["home", "dome"],
            ["gains", "snake"],
            ["gamble", "maples"],
            ]
    
    for example in examples:
        print(S.isogram_matcher(example[0], example[1]))
    
    
    
    
    
    
    
                    