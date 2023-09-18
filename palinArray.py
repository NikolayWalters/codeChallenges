# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. 
# Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def PalinArray(arr):
    """Check if all elements in the array are palindrome numbers."""
    for num in arr:
        if not is_palindrome(num):
            return 0
    return 1

# Testing the function with the provided example
test_array = [111, 222, 333, 444, 555]
PalinArray(test_array)
