### Description 

In the hash_table_task file, there are classic problems involving Dictionaries and Sets. 

### 1. Count Occurrences

The function count_occurrences receives a collection of `words` and returns a Dictionary which describes how many times each word occurs
```
words: ['John', 'Mike', 'John']
returns: { 'John': 2, 'Mike': 1 }
```

### 2. Two Sum 

The function two_sum takes a collection of `numbers` and a `target_sum` and returns the indices of the first two numbers that add up to the given `target_sum` as a tuple. If no such numbers exist, returns `(-1, -1)`.
```
numbers: [3, 0, 2, 4, 1]
sum: 7
returns: [0, 3]
```

#### Approach #1 (Naive, time: O(n*n), space: O(1))
Using two nested loops, for each number in the list, we can search for a corresponding number, stopping when a match is found
```pseudo
for i of nums
   for j of nums
      if nums[i] + nums[j] == target
          return i,j

return -1, -1
```
These approach is not optimal. We are starting a loop for each number in the list, leading to **n*n** complexity.
No additional memory is required.

#### Approach #2 (time: O(n), space: O(n))
Using a dict that stores each encountered number along with its index, we can remember if we have *seen* a particular number.
1. For example, while iterating, you can use the **current number** and the **target_sum** and perform a **very simple calculation** to find the other number.
2. If we have *seen* that other number, we also know its index and we can immediately return the answer.

- Time: O(n) - only one pass through the collection is enough
- Space: O(n) - we need to maintain a dict that grows as the collection grows

> The faster approach requires more memory: This is a common theme with algorithms - the faster ones usually `remember` some information, resulting in additional memory consumption.

### 3. Special Coins

The function special_coins takes a string of `coins` (where each coin is represented by a letter) and a `catalogue` string, representing special coins. Find the number of unique coins in the first string
```
coins: 'aaAb'
catalogue: 'ab'
returns: 3 // we have 'a' twice and 'b' once (it's case sensitive)

```
#### Approach I (Naive, O(m*n))
For each coin in the `coins` string, we can search inside the `catalogue` string. Searching in a string (either with `index` or `in` has **O(n)** complexity), resulting in total running time of **O(m * n)** where `m` is the length of the `coins` string and `n` is the length of the `catalogue` string.

#### Approach II (Using sets, O(m+n))
Sets provide extremely fast search **O(1)**, which means that we can **first build a set** from the `catalogue` string.
Then, for each coin, check if the set `has` such a special coin.
This results into a running time of `n` (for building the set) + `m` (for iterating the `coins` string).

> The second approach is **MUCH** faster. For example, with 10000-long `coins` and a 1000-long `catalogue`:
> - **O(m*n) solution**: 10000 * 1000 -> 10000000 (10 million operations)
> - **O(m+n) solution**: 10000 + 1000 -> 11000 (11 thousand operations)

### 4. Isomorphic strings

Two strings are considered isomorphic if each character in `s1` can map to a character in `s2` 
```
s1: egg
s2: add
returns: true // e -> a, g -> d

s1: egge
s2: addb
returns: false // e cant map to both a and b for the unique pair (egge, addb)
```