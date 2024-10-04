'''
Write a program that counts how many times the number 11 appears in a given array starting from a specified index.

Requirements:
Your program should define a function that uses recursion.
The function should return the count of occurrences of '11' in the array starting from index n; 
The program should take a comma-separated list of integers as input for the array 
and an integer input for the starting index n, then print the result of the function.
'''

def arrays_containing11(array, n):
    if len(array) <= n:
        return 0
    if array[n] == 11:
        return 1 + arrays_containing11(array, n + 1)
    else:
        return arrays_containing11(array, n + 1)

array = [int(n) for n in input().split(",")]
n = int(input())
print(arrays_containing11(array, n))