'''
Write a program that checks whether the number 6 appears in a given array starting from a specific index. 

Requirements:
Your program should define a function that uses recursion.
The function should return "true" if the number 6 is found in the array starting from index n; 
otherwise, it should return "false".
If the index n is equal to or greater than the length of the array, the function should return "false" 
The program should take a comma-separated list of integers as input for the array 
and an integer input for the starting index n, then print the result of the function.
'''

def array_with6(array, n):
    if len(array) <= n:
        return "false"
    if array[n] == 6:
        return "true"
    else:
        return array_with6(array, n + 1)


array = [int(n) for n in input().split(",")]
n = int(input())
print(array_with6(array, n))