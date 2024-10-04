'''
You are in charge of a small bunny farm. Each bunny has exactly two ears. 
Write a recursive function that calculates the total number of bunny ears given the number of bunnies.

Requirements:
The function should handle the base case where there are 0 bunnies (i.e., bunny_ears(0) should return 0).
The program should take an integer input from the user and print the total number of ears.
'''

def bunny_ears(bunies):
    if bunies == 0:
        return 0
    
    return 2 + bunny_ears(bunies - 1)

bunies = int(input())
print(bunny_ears(bunies))