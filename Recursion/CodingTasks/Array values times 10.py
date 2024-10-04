'''
Write a program that checks whether there is at least one element in a given array that is a multiple of 10.

Requirements:
Your program should define a function that uses recursion.
Returns "true" if a multiple of 10 is found, otherwise returns "false".
If the index n is equal to or greater than the length of the array, return "false" 
The program should take a comma-separated list of integers as input for the array 
and an integer input for the starting index n, then print the result of the function.
'''

def array_values_times10(array, n):
    if len(array) <= n:
        return "false"
    if array[n] % 10 == 0 :
        return "true"
    else:
        return array_values_times10(array, n+1)

array = [int(n) for n in input().split(",")]
n = int(input())
print(array_values_times10(array, n))