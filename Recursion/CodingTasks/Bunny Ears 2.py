'''
You are managing a farm where there are two types of bunnies:
Odd-numbered bunnies (1st, 3rd, 5th, etc.) have 2 ears each.
Even-numbered bunnies (2nd, 4th, 6th, etc.) have 2 ears each and one raised foot 
(so let's say that they have 3 ears each).

Requirements:
The function should use recursion to calculate the total number of ears based on the number of bunnies.
The function should handle the base case where there are 0 bunnies (i.e., bunny_ears_2(0) should return 0).
The program should take an integer input from the user and print the total number of ears.
'''

def bunny_ears_2(bunies):
    if bunies == 0:
        return 0
    if bunies % 2 == 0:
        return 3 + bunny_ears_2(bunies - 1)
    return 2 + bunny_ears_2(bunies - 1)

bunies = int(input())
print(bunny_ears_2(bunies))