def find_index_linear(t, nums):
    for i in range(len(nums)):
        if t == nums[i]:
            return i
    return False


nums = [11, 23, 8, 14, 30, 9, 6, 17, 22, 28]
print(find_index_linear(30, nums))
print(find_index_linear(13, nums))