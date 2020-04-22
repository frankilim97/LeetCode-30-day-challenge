#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:29:46 2020

@author: francescalim
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # create a dictionary with key n (value can be anything so just assign n)
        d = {n:n} 
        happy = n 
        # Use a while loop because you don't know how many iterations you need
        while True:
            # convert the input value n to a string
            # then int() allows you to obtain a list of the characters of the string 
            # we immediately square these numbers
            # replace happy variable with the sum of these numbers
            happy = sum([int(d)**2 for d in str(happy)])
            # iterate over this until the value of happy is 1 
            if happy == 1:
                return True
            # Check if the number is already in the dictionary, if it is then 
            # stopt the loop, otherwise add the number to the dictionary 
            if happy in d:
                return False
            d[happy] = happy
            
