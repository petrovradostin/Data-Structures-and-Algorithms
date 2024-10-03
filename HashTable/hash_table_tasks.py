
def count_occurrences(words: list) -> dict:
    output_dict = {}
    for word in words:
        if word in output_dict:
            output_dict[word] += 1
        else:
            output_dict[word] = 1
    return output_dict

def two_sum(numbers: list, target_sum: int) -> tuple:
    output_dict = {}
    for i, num in enumerate(numbers):
        co = target_sum - num
        if co in output_dict:
            return (output_dict[co], i)
        output_dict[num] = i
    return (-1, -1)
        
def special_coins(coins: str, catalogue: str) -> int:
    count = 0
    cat_set = set()
    for ch in catalogue:
        cat_set.add(ch)
    for coin in coins:
        if coin in cat_set:
            count += 1
    return count
 
def are_isomorphic(s1: str, s2: str) -> bool:
    str_dict = {}
    s2_added = set()
    if len(s1) != len(s2):
        return False
    for ch1, ch2 in zip(s1, s2):
        if ch1 in str_dict:
            if str_dict[ch1] != ch2:
                return False
        else:
            if ch2 in s2_added:
                return False
            str_dict[ch1] = ch2
            s2_added.add(ch2)
    return True

