# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:08:11 2025

@author: PC1
"""

import random


def number_guessing_game():
    count =1
    num = random.randint(0, 100)
    print(num)
    n = int(input("Enter a number that matchs random generated num:"))
    while True:
        if num == n:
            print("Number matchs: ")
            break
        elif n > num:
            n= int(input("Num is greather than random generated num,try again:"))
            count +=1
            continue
        else:
            n= int(input("Num is less than random generated num,try again:"))
            count+=1
            continue
    print("Attempt:",count)
number_guessing_game()

    