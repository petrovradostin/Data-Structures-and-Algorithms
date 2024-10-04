'''
Write a program that counts the occurrences of the digit '8' and the double digits '88' in a given number. 
For example the digit '88' should be counted as two occurrences of '8' and on of '88'.

Requirements:
Your program should define a function that uses recursion.
The base case is when the number becomes 0 (i.e., count_occurrences2(0) should return 0).
The program should take an integer input from the user and print the total count of '8's based on the rules above.
'''

def count_occurrences2(n):
    if n == 0:
        return 0
    elif n % 100 == 88:
        return 2 + count_occurrences2(n // 10)
    elif n % 10 == 8:
        return 1 + count_occurrences2(n // 10)
    else:
        return count_occurrences2(n // 10)
    
n = int(input())
print(count_occurrences2(n))