# Sorting Algorithms

## 1. Selection sort
Finds the smallest element in the array and moves it to the front of the array. Then repeats this process with the rest of the elements.
- Worst-case: We must iterate over each of the 𝒏 elements of the array (to find the smallest unsorted element), and we must repeat this process 𝒏 times, since only one elements gets sorted on each pass.
The time complexity is O(𝒏^𝟐).
- Best-case: Same as worst-case! All steps are performed even if the array is already sorted.

## 2. Bubble sort
Moves heavier elements toward the right side and lighter elements toward the left side.
- Worst-case: The array is reversed. We must bubble each of the 𝒏 elements all the way across the array, and since we can bubble only one element, we must do this 𝒏 times. 
The time complexity is O(𝒏^𝟐).
- Best-case: The array is already sorted, so we make no swaps on the first pass.

## 3. Merge sort
Splits the array in halves, sorts them recursively and then combine them together (merge them) in sorted order.
Divide and conquer!
- Worst-case: We must split 𝒏 elements down to single elements (𝒍𝒐𝒈⁡𝒏 times) and then recombine them (in 𝒏 steps), effectively doubling the sorted subarrays as we build them up. 
The time complexity is O(𝒏 𝒍𝒐𝒈⁡𝒏)
- Best-case: The array is already sorted though we still must split and recombine it back together.

## 4 Quick sort
Selects a random element as pivot. Then puts the smaller elements on the left of the pivot and the larger ones on the right.
- Worst-case: When the smallest or largest element is selected as pivot. 
The time complexity is O(𝒏^𝟐)
- Best-case: When partitions have the same size.
