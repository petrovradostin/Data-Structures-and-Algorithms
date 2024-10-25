# Searching Algorithms

## 1. Linear Search
Iterate across the collection from left to right. On each step, check if the element is the target. Stop iteration if true and return the element. If no more elements remain  →  the answer is False.
- Worse-case scenario: We must look through the entire array of n elements, either because the target element is the last element of the array or doesn’t exist in the array at all.
The time complexity is O(n)
- Best-case scenario: The target element is the first element of the array, and so we can stop looking immediately after we start.

## 2. Binary Search
This algorithm requires that the array is sorted. Check if the middle element is the target. If not, apply the same logic for either the left or right half of the array. Each step divides the array into two halves.
- Worse-case scenario: Divide the list of n elements in half repeatedly, either because the target element will be found at the end of the last division or it doesn’t exist in the array at all.
The time complexity is O(log n)
- Best-case scenario: The target element is at the midpoint of the full array, and so we can stop looking immediately after we start.




