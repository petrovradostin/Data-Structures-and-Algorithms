'''
Write a program that replaces every occurrence of the substring "pi" in a given string with "3.14".

Requirements:
Your program should define a function that uses recursion.
The base case is when the length of the string is less than 2
(i.e., change_pi('') or change_pi('a') should return the string itself).
The program should take a string input from the user and print the modified string.
'''

def change_pi(string):
    if len(string) < 2:
        return string
    elif  string[:2] == "pi":
        return "3.14" + change_pi(string[2:])
    else:
        return string[0] + change_pi(string[1:])
    
string = input()
print(change_pi(string))