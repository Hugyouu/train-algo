# PATTERN : PREFIX SUFFIX

def productExceptSelf(nums: list[int]) -> list[int]:
    arr = [1]*len(nums)
    
    left = 1    
    for i in range(len(nums)):
        arr[i] = left
        left *= nums[i]
        
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        arr[i] *= right
        right *= nums[i]
    
    return arr

# nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
nums = [0, 0]
print(productExceptSelf(nums))