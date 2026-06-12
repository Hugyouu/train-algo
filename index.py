from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    if nums[mid] > target:
        return mid - 1
    return mid + 1

if __name__ == "__main__":
    print(searchInsert([1, 3, 5, 7], 8))