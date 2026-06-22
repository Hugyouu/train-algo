def removeDuplicates(nums: list[int]) -> int:
    result = nums.copy()
    for num in nums:
        if result.count(num) > 1:
            result.remove(num)
    print(result)
    return len(result)



removeDuplicates([1,1,2])