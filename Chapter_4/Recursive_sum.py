# 4.1 Write out the code for the earlier sum function.

def sum(nums: list[int]) -> int:
    # Base Case
    if len(nums) <= 0:
        return 0
    
    # Recursive Case
    return nums[0] + sum(nums[1:])


# Test case
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))