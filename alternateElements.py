# You are given an array A of size N. 
# You need to print elements of A in alternate order (starting from index 0).

# Example 1:

# Input:
# N = 4
# A[] = {1, 2, 3, 4}
# Output:
# 1 3

def print_alternate_elements(arr):
    """Print elements of an array in alternate order starting from index 0."""
    return arr[::2]

# Testing the function with the provided example
test_array = [1, 2, 3, 4]
print_alternate_elements(test_array)

# NB to go from [1, 2, 3, 4] -> [2, 4]
# can use arr[1::2]