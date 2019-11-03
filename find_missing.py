#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:40:26 2019

@author: bijayamanandhar
"""
def to_camel_case(text):
    #your code here
    x = ""
    
    for char in text:
        if char in "_-":
            x = char
    text = text.split(x)
    new = [text[0]]
    
    for i in range(1, len(text)):
        word = text[i].capitalize()
        new.append(word)
        
    return ''.join(new)

print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))

