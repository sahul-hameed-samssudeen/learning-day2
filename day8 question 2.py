# -*- coding: utf-8 -*-
"""test 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V3WbG0ePvDm5qZGIhXTjgaIVmdiF42YW
"""

# math_operations.py
pi=3.14159
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")
a=int(input("enter a"))
b=int(input("enter b"))
print(f"Addition:  = {add(a, b)}")
print(f"subtraction = {subtract(a,b)}")
print(f"division")