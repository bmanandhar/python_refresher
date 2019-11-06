#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:45:09 2019

@author: bijayamanandhar
"""

"""
Write a function 'string_reverse' that takes a string of different
words and returns a string with the words in reversed order.
Example: 
    input string: "teacher loves coffee"
    output string: "coffee loves teacher"
"""

class Solution:

    def string_reverse(self, sentence):
        
        words = sentence.split(' ')   #words are split and placed in a list
        string = []
        
        for word in words:
            string.insert(0, word)    #words in the list are reversed
        
        return ' '.join(string)       #returns the string that is reversed


if __name__ == "__main__":
    
    S = Solution()
    examples = (
            "teacher loves coffe",
            "she will go to school",
            "my father is working",
            "wife is in the city"
            )
    for example in examples:

        print(S.string_reverse(example))
        
        
        