#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:01:17 2019

@author: bijayamanandhar
"""
import datetime 
#start time 
import time
print(time.localtime())
x = datetime.datetime.now()
print('Start time: ', x)
#code starts below
      
#code ends here     
#end time = y
y = datetime.datetime.now()
print('End time: ', y)



x = [1,2,3,6]
print(x.index(2))

x = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
print(x['M'])


arr = [1,2,2,3,3,4,4,4,4]

print(arr.count(4))

print(len(''*3))

"""
Write a function that takes a string of different words
and returns a string with words in reversed order.
Example: 
    input string: "teacher loves coffee"
    output string: "coffee loves teacher"
"""

class Solution:

    def string_reverse(self, sentence):
        
        words = sentence.split(' ')
        string = []
        
        for word in words:
            string.insert(0, word)
        
        return ' '.join(string)


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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
