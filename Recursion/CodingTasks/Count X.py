'''
Write a program that counts how many times the character 'x' appears in a given string.

Requirements:
Your program should define a function  that uses recursion.
The base case is when the string becomes empty (i.e., count_x('') should return 0).
The program should take a string input from the user and print the number of occurrences of the character 'x'.
'''

def count_x(string):
    if len(string) == 0:
        return 0
    elif string[0] == "x":
        return 1 + count_x(string[1:]) 
    else:
        return count_x(string[1:])
    
string = input()
print(count_x(string))