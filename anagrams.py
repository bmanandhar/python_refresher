#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:58:28 2019

@author: bijayamanandhar
"""
"""
Description:
What is an anagram? Well, two words are anagrams of each other
if they both contain the same letters. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

class Solution(object):

    def anagrams(self, check_word, array):
        
        anagram_words = []
        
        check_word_dictionary = self.helper(check_word)
        
        for each_word in array:
            
            each_word_dictionary = self.helper(each_word)
            
            if each_word_dictionary == check_word_dictionary:
                anagram_words.append(each_word)
                
        return anagram_words
        
    
    #helper function
            
    def helper(self, word):
        
        dictionary = {}        
        
        for char in word: 
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        return dictionary
    
    
if __name__== "__main__":
    
    S = Solution()
    examples = [
            ['racer', ['crazer', 'racer']],
            ['racer', ['crazer', 'carer', 'racar', 'caers', 'racer']],
            ['abba', ['aabb', 'abcd', 'bbaa', 'dada']],
            ['laser', ['lazing', 'lazy',  'lacer']],
            ['funeral',['funreal', 'realfunny', 'realfun', 'funnyreal']]
             ]

    for example in examples:
        print(S.anagrams(example[0], example[1]))




    
    