'''
Write a program that takes a single integer input from the user and calculates its factorial. 
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
The factorial of 0 is defined as 1.

Requirements:
Your program should define a function which uses recursion to calculate the factorial of the given number.
The function should handle the base case of 0 (i.e., factorial(0) should return 1).
The program should take an integer input from the user and print the calculated factorial.
'''

def factorial(input: int):
    if input == 0:
        return 1
    return input * factorial(input - 1)
    
    
input = int(input())
print(factorial(input))