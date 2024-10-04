'''
Write a program that calculates the sum of the digits of a given number. 

Requirements:
Your program should define a function  that uses recursion to calculate the sum of the digits of an integer.
The base case is when the integer is 0 (i.e., sum_digits(n) should return 0).
The program should take a numeric input and print the sum of those digits.
'''

def sum_digits(n):
    if n == []:
        return 0
    first, *rest = n

    return first + sum_digits(rest)

n = [int(n) for n in (input())]
print(sum_digits(n))