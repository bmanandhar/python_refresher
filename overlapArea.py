#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:55:35 2019

@author: bijayamanandhar
"""

"""
Given two overlapping rectangles on a plane.
We are given bottom left and top right points of the two rectangles. 
We need to find the total area overlapped by the rectangles.

                   .-----------.
                   |           |
                   |           |
            .------|-----------| 
            |      |...........|
            |      |...........|
            |      |...........|
            |      .-----------|            
            |                  |
            |                  |
            .------------------.

"""
class Solution:
    
    
    def overlapArea(self, rect1, rect2):
    
        x_min = max(rect1[0][0], rect2[0][0])
        x_max = min(rect1[1][0], rect2[1][0])
    
        y_min = max(rect1[0][1], rect2[0][1]) 
        y_max = min(rect1[1][1], rect2[1][1])
        
        if x_min > x_max:
            return False
        
        return (x_max - x_min) * (y_max - y_min)
    
if __name__ == '__main__':
    
    S = Solution()

    print("Test for rec intersection")
    print('- - - - - - -')
    print(S.overlapArea([[0, 0], [2, 1]], [[1, 0], [3, 1]]))
    print(S.overlapArea([[1, 1], [2, 2]], [[0, 0], [5, 5]]))
    print(S.overlapArea([[1, 1], [2, 2]], [[4, 4], [5, 5]]))
    print(S.overlapArea([[1, 1], [5, 4]], [[2, 2], [3, 5]]))



    
