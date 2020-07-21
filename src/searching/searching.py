# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # if array is empty...return -1...won't find target
    if len(arr) == 0:
        return -1
    
    # find midpoint value
    midpoint = (start + end)//2
    
    # base case: when target is found, i.e., when midpoint is the target value
    if arr[midpoint] == target:
        return midpoint

    # if you go thru all the numbers in the array and you don't find the target, return -1 (not found)
    if start == end and arr[midpoint] != target:
        return -1

    else: 
    # recursive case: call function again with either new start or end values depending on if target is less than or greater than midpoint
        # if midpoint is greater than target...eliminate RHS
        if arr[midpoint] > target: 
            # call functino again & update end value with midpoint
            return binary_search(arr, target, start, midpoint)
        # else midpoint is less than target...eliminate LHS
        else: 
            # call function again & update start value with midpoint + 1
            return binary_search(arr, target, (midpoint + 1), end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
