#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:32:49 2019

@author: bijayamanandhar
"""

""" 
A bigram of a sentence is defined as the sum of two adjacent words.
For example, for the sentence "One must have a mind of winter", 
possible bigrams are
'One must', 'must have', 'have a', 'a mind', 'mind of', and 'of winter'.

Write a function that returns the longest bigram.
"""

class Solution(object):
    
    def longest_bigram(self, sentence):
        
        split_sentence = sentence.split()  
        
        longest_bigram = ""
        for i in range(len(split_sentence) - 1):
            
            x = split_sentence[i] + " " + split_sentence[i+1]
            
            if len(x) > len(longest_bigram):
                
                longest_bigram = x
                
        return longest_bigram
        
if __name__ == "__main__":
    
    S = Solution()
    
    examples = (
            ("One must have a mind of winter"),        #must have
            ("Where there is a will there is a way"),  #Where there
            ("Sky is the limit"),                      #the limit
            ("Make hay while the sun shines"),             #sun shines
            ("A stitch in time saves nine")            #time saves
            )
    for example in examples:
        print(S.longest_bigram(example))
    
    
    
    