# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:31:57 2022

@author: Yvonne
"""

def star(layers):
    for i in range(1, layers + 1):
        print('*' * i)
        

# define 一個 function，把3個數字相加
def add_three(num1, num2, num3):
    total = num1 + num2 + num3
    return total

number = add_three(1, 2, 3)
print(number)