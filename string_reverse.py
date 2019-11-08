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
            "teacher loves coffe",     #"coffe loves teacher"
            "she will go to school",   #"school to go will she"
            "my father is working",    #"working is father my"
            "wife is in the city"      #"city the in is wife"
            )
    i = 0
    while i < len(examples):

        print(S.string_reverse(examples[i]))
        i += 1
        
        