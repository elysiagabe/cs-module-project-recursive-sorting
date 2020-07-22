# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    """FIRST BAD SOLUTION -- BLAH
    # Your code here
    # initialize index at 0...this will refer to index of merged_arr
    i = 0
    # while the index is less than the length of the array
    while i <= len(merged_arr):
        # if no elements in arrA,
        if len(arrA) == 0:
            # remove the first element from arrB and insert at index
            merged_arr[i] = arrB.pop(0)
        # else if no elements in arrB,
        elif len(arrB) == 0:
            # remove first element from arrA and insert at index
            merged_arr[i] = arrA.pop(0)
        # else if value at beginning of arrA is less than value at beginning of arrB,
        elif arrA[0] < arrB[0]:
            # remove from arrA and insert at index
            merged_arr[i] = arrA.pop(0)
        # else if value at beginning of arrB is less than value at beginning of arrA,
        elif arrB[0] < arrA[0]:
            # remove from arrB and insert at index
            merged_arr[i] = arrB.pop(0)
        #increment index after any of the above take place to move on to next value of merged array
        i += 1
    """
    """SECOND SOLUTION"""
    # # initialize index pointers at 0
    # # i will point to arrA index, j will point to arrB index, and k will point to merged_arr index
    i = j = k = 0
    
    # while there are still elements to sort in both arrA & arrB,
    while i < len(arrA) and j < len(arrB):
        # compare values of the first elements of arrA & arrB...add whichever one is less to merged_arr
        # increment index pointers as needed
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    
    # if there are only unsorted values in arrA, add them to merged_arr in order and increment index pointers as needed
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    # opposite of the above
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # if length of given array is less than 2, there's nothing to sort. Return the arr as is. 
    if len(arr) < 2:
        return arr
    
    # initialize middle value to break into 2 halves
    middle = len(arr)//2

    # this splits the array into 2 based on middle value...and then it'll keep breaking up arrays until each one has length 1...I think....
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    # merge everything back together again
    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
