import time


def helper(message, value):
    print(message, value)
    time.sleep(1)

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # Sorting happens here...
    # Place element 0 in arrA
    a = 0
    b = 0

    for c in range(0, elements):
        # start comparisons
        # If a is out of range, push b and iterate.
        if a >= len(arrA):
            # we're done with a, push b
            merged_arr[c] = arrB[b]
            b += 1
            helper("merged_arr when a >= len(arr)", merged_arr)
        # If b is out of range, push a and iterate.
        elif b >= len(arrB):
            merged_arr[c] = arrA[a]
            a += 1
            helper("merged_arr when b >= len(arr)", merged_arr)
        # If a is smaller place into merged_arr at index c and iterate both.
        elif arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
            helper("merged_arr arrA[a] < arrB[b]", merged_arr)
        # If b is smaller place into merged_arr at index c and iterate both.
        elif arrA[a] > arrB[b]:
            merged_arr[c] = arrB[b]
            b += 1
            helper("merged_arr arrA[a] > arrB[b]", merged_arr)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

    # What is the base case?
    # if arr size is > 1? Return.
    if len(arr) > 1:
        # Split the array in half until there are only one values in the array. This is the base case.
        # Sort then Add elements to the right
        left = merge_sort(arr[0:len(arr)//2])
        # Sort then Add elements to the left
        right = merge_sort(arr[len(arr)//2:])

        # merge left and right
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


test = [6, 3, 7, 2, 1, 8, 9, 4, 10, 5]
print(merge_sort(test))
