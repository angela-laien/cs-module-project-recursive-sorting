# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0
    m = 0
    # Make sure starting index is less than length of array
    while a < len(arrA) and b < len(arrB):
        # If arrA at the given index is less than or equal to arrB at the given index
        if arrA[a] <= arrB[b]:
            # Take the given index in the merged array and set it to the element of arrA given index
            merged_arr[m] = arrA[a]
            # Increase the index on arrA by 1
            a = a + 1
        # If the arrA element at the given index is greater than the arrB element at the given index
        else:
            # Take the given index in the merged array and set it to the element of the arrB given index
            merged_arr[m] = arrB[b]
            # Increase the index on arrB by 1
            b = b + 1
        # Increase the index on merged array by 1
        m = m + 1
    
    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a = a + 1
        m = m + 1
    
    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b = b + 1
        m = m + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        midpoint = len(arr) // 2
        arrA = arr[:midpoint]
        arrB = arr[midpoint:]

        if len(arrA) > 1:
            arrA = merge_sort(arrA)
        if len(arrB) > 1:
            arrB = merge_sort(arrB)

        arr = merge(arrA, arrB)
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

