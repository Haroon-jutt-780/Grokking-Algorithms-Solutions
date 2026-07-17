"""
  4.4 Remember binary search from chapter 1? Its a divide-and-conquer 
  algorithm, too. Can you come up with the base case and recursive 
  case for binary search?
"""

def binary_search(arr: list[int], target: int, low: int, high: int) -> int:
    #Base Case if target not found
    if low > high:
        return -1
    
    mid = (low + high) // 2

    #Base case if target found
    if arr[mid] == target:
        return mid
    
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
    

# Test Case
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3, 0, len(my_list) - 1))  # Output: 1