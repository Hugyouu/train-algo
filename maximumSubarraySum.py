# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

#     The length of the subarray is k, and
#     All the elements of the subarray are distinct.

# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

def maximumSubarraySum(nums: list, k: int):
    max_sum = 0
    for i in range(len(nums)-k+1):
        sub_array = nums[i:i+k]
        if len(sub_array) == len(set(sub_array)):
            max_sum = max(max_sum, sum(sub_array))
    return max_sum


if __name__ == "__main__":
    nums = [9,9,9,1,2,3]
    print(maximumSubarraySum(nums, 3))