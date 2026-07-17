#4.2 Write a recursive function to count the number of items in a list.
def count(nums: list[int]) -> int:

    #Base Case
    if len(nums) == 0:
        return 0
    
    #Recursive case
    return 1 + count(nums[1:])

#Test case
nums = [1, 3, 5, 7, 9]
print(count(nums))