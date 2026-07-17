#4.3 Find the maximum number in a list.
def find_max(nums: list[int]) -> int:

    #Base Case
    if len(nums) == 1:
        return nums[0]
    
    #Recursive case
    sub_max = find_max(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max

#Test case
nums = [1, 3, 5, 7, 9]
print(find_max(nums))
