# Find the maximum sum of a subarray of length k where all elements are distinct.
# Return 0 if no such subarray exists.

def maximumSubarraySum(nums: list, k: int) -> int:
    max_sum = 0
    for i in range(len(nums) - k + 1):
        sub_array = nums[i:i+k]
        if len(sub_array) == len(set(sub_array)):
            max_sum = max(max_sum, sum(sub_array))
    return max_sum

# TODO: use a dict to optimized