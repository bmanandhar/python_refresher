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

    
x = [1, 'a', 4, 'b', 9, 'g']
    
print(x)
    
x = list(reversed(x))  
    
print(x, 'reversed')   
print(x.index(4))

print(" ")
class Person():
    
    def __init__(self, name, age, city, job):
        self.name = name
        self.age = age
        self.city = city
        self.job = job
        
    def show(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("City: ", self.city)
        print("Job: ", self.job)
        
peter = Person("Peter", 21, "Denver", "Web developer")
michelle = Person("Michelle", 20, "Oakland", "Photographer")

peter.show()
print(" ")
michelle.show()
       
class this_is_class:
    
    def show(self):
        print("Example of class!")

this = this_is_class()
print(" ")
this.show()


      

      
      

