'''
Write a program that counts how many times the 'hi' appears in a given string.

Requirements:
Your program should define a function that uses recursion.
The base case is when the string becomes empty (i.e., count_x('') should return 0).
The program should take a string input from the user and print the number of occurrences of the 'hi'.
'''

def count_hi(string):
    if len(string) == 1:
        return 0
    elif string[0] == "h" and string[1] == "i":
        return 1 + count_hi(string[1:])
    else:
        return count_hi(string[1:])


string = input()
print(count_hi(string))