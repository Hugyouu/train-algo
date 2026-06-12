# Find the maximum sum of a subarray of length k where all elements are distinct.
# Return 0 if no such subarray exists.

def maximumSubarraySum(nums: list, k: int) -> int:
    max_sum = None
    for i in range(len(nums) - k + 1):
        sub_array = nums[i:i+k]
        if len(sub_array) == len(set(sub_array)):
            s = sum(sub_array)
            max_sum = s if max_sum is None else max(max_sum, s)
    return max_sum if max_sum is not None else 0


if __name__ == "__main__":
    print(maximumSubarraySum([9, 9, 9, 1, 2, 3], 3))
