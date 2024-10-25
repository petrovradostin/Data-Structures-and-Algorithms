def binary_search_iter(t, nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < t:
            start = mid + 1
        elif nums[mid] > t:
            end = mid - 1
        else:
            return mid
    return False

nums = [6, 8, 9, 11, 14, 17, 22, 23, 25, 28, 30]
print(binary_search_iter(6, nums))
print(binary_search_iter(11, nums))
print(binary_search_iter(30, nums))
print(binary_search_iter(15, nums))