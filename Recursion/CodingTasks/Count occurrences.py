'''
Write a program that counts how many times the digit '7' appears in a given number. 

Requirements:
Your program should define a function that uses recursion.
The base case is when the number becomes 0 (i.e., count_occurrences(0) should return 0).
The program should take an integer input from the user and print the number of times the digit '7' appears in the input.
'''

def count_occurrences(n):
    if n == 0:
        return 0
    elif n % 10 == 7:
        return 1 + count_occurrences(n // 10)
    else:
        return count_occurrences(n // 10)

n = int(input())
print(count_occurrences(n))