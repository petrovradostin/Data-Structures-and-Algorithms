'''
Imagine you are building a triangle out of blocks, where the first row has 1 block, 
the second row has 2 blocks, the third row has 3 blocks, and so on. 
Write a recursive function that calculates the total number of blocks in a triangle that has a given number of rows.

Requirements:
The function should handle the base case where there are 0 or 1 rows 
(i.e., triangle(0) should return 0, and triangle(1) should return 1).
The program should take an integer input from the user and print the total number of blocks.
'''

def triangle(rows):
    if rows <= 1:
        return rows
    return rows + triangle(rows - 1)

rows = int(input())
print(triangle(rows))