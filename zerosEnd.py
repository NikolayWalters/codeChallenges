"""
Given an array of random numbers, Push all the zero’s of a given array 
to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, 
it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements 
should be same. Expected time complexity is O(n) and extra space is O(1).
"""

def move_zeros_to_end(nums):
    last_non_zero = 0
    
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero], nums[current] = nums[current], nums[last_non_zero]
            last_non_zero += 1
            
    return nums

# Test
test_array = [0, 1, 0, 3, 12]
print(move_zeros_to_end(test_array))
