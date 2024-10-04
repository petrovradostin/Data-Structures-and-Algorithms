'''
Write a program that calculates the result of raising a base number to a power using recursion. 
The program should recursively multiply the base number by itself n times to calculate base^n.

Requirements:
The base case is when the power is 0 (i.e., power_n(base, 0) should return 1).
The program should take two integer inputs from the user: 
the base number and the power, and then print the result of base^n.
'''

def power_n(base, n):
    if n == 0:
        return 1
    return base * power_n(base, n - 1)

base = int(input())
n = int(input())
print(power_n(base, n))