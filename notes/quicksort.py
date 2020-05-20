# Divide and conquer


# def partition(data):
#     pivot = data[0]
#     left = []
#     right = []

#     for x in data[1:]:
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)

#     return left, pivot, right


# def quicksort(data):
#     if len(data) == 0:
#         return data

#     left, pivot, right = partition(data)

#     return quicksort(left) + [pivot] + quicksort(right)

# In-place quicksort
def partition(data, start, end):
    pivot = data[start]

    i = start + 1
    j = start + 1

    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1

    data[start], data[i-1] = data[i-1], data[start]

    return i - 1


def quicksort(data, start=0, end=None):
    if end is None:
        end = len(data) - 1

    if len(data) == 0:
        return data

    index = partition(data)
