#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:10:01 2019

@author: bijayamanandhar
"""
'''
array is the record of bird sighting in frequesncy, elements being bird-id
n is the total number of bird types (id) ranging from 1 thru n
'''

class Solution:
    # Complete the migratoryBirds function below.
    def migratoryBirds(self, arr, n):
        
        #creates a dictionary for types of birds as key and total of that type as value
        #creates a variable for result
        #creates a vriable for number of occurences
        
        #different variables
        bird_dic, result, freq = {}, '', 0
    
        #types of birds, id-1 thru id-n
        for i in range(1, n+1):
    
            #forms a dictionary with key-value pairs for types of birds and occurences
            bird_dic[i] = arr.count(i)
        #checking occurences with respect to types of birds
        for key in bird_dic:
            
            #sets condition for updating result
            if bird_dic[key] > freq: 
                
                result, freq = key, bird_dic[key] 
        
        return result 

if __name__ == '__main__':
    
    S = Solution()

    print(S.migratoryBirds([1,3,5,3,4,1,4,4,5,5,3,3], 5) == 3) #should print 'True'


