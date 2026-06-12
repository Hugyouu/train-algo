# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

#     The length of the subarray is k, and
#     All the elements of the subarray are distinct.

# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

def maximumSubarraySum(nums: list, k: int):
    max_sum = 0
    for i in range(len(nums)-k+1):
        sub_array = []
        if i + k <= len(nums):
            for n in range(k):
                sub_array.append(nums[i+n]) 
        sub_array = set(sub_array)
        print(sub_array)
        if max_sum < sum(sub_array):
            max_sum = sum(sub_array)
    return max_sum


if __name__ == "__main__":
    nums = [1,5,4,2,9,9,9]
    print(maximumSubarraySum(nums, 3))