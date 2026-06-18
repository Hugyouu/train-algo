# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3


def longuest_consecutive(nums: list[int]):
    set_nums = set(nums)
    max_length = 0
    for num in set_nums:
        if num-1 not in set_nums:
            current = num
            count = 1
            while current+1 in set_nums:
                count += 1
                current += 1
            if max_length < count:
                max_length = count
    return max_length

nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [1,0,1,2]

print(longuest_consecutive(nums))