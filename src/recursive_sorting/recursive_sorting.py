import time


def helper(message, value):
    print(message, value)
    time.sleep(1)

# TO-DO: complete the helper function below to merge 2 sorted Ays


# Sorting happens here...
def merge(Left, Right):
    # elements = len(Left) + len(Right)
    # Left index, and right index
    li = 0
    ri = 0

    # Seans way
    combined = []
    while li < len(Left) and ri < len(Right):
        if Left[li] < Right[ri]:
            combined.append(Left[li])
            li += 1
        else:
            combined.append(Right[ri])
            ri += 1

    while li < len(Left):
        combined.append(Left[li])
        li += 1

    while ri < len(Right):
        combined.append(Right[ri])
        ri += 1

    return combined

    # Bryans way
    # merged_arr = [0] * elements
    # for c in range(0, elements):
    #     # start comparisons
    #     # If a is out of range, push b and iterate.
    #     if a >= len(A):
    #         # we're done with a, push b
    #         merged_arr[c] = B[b]
    #         b += 1
    #     # If b is out of range, push a and iterate.
    #     elif b >= len(B):
    #         merged_arr[c] = A[a]
    #         a += 1
    #     # If a is smaller place into merged_arr at index c and iterate both.
    #     elif A[a] < B[b]:
    #         merged_arr[c] = A[a]
    #         a += 1
    #     # If b is smaller place into merged_arr at index c and iterate both.
    #     elif A[a] > B[b]:
    #         merged_arr[c] = B[b]
    #         b += 1
    # return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

    # What is the base case?
    # if arr size is > 1? Return.
    if len(arr) > 1:
        # Split the Ay in half until there are only one values in the Ay. This is the base case.
        # Sort then Add elements to the right
        left = merge_sort(arr[0:len(arr)//2])
        # Sort then Add elements to the left
        right = merge_sort(arr[len(arr)//2:])

        # merge left and right
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # start2 is the first element in the right
    # half of the list
    start2 = mid + 1

    # If the two halves we're merging are already
    # sorted, no need to do anything
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:  # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
    return arr

# we don't return anything in in-place functions
# since we're directly mutating the input array


def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


test = [6, 3, 7, 2, 1, 8, 9, 4, 10, 5]
print(merge_sort(test))
print(merge_sort_in_place(test, 0, len(test) - 1))
