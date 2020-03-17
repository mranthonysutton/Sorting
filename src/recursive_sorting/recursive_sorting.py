# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # sets temp indexes to allow for index to be assigned
    a_index = 0
    b_index = 0

    # TO-DO
    for i in range(elements):
        # checks if all of a have been merged
        if a_index >= len(arrA):
            merged_arr[i] = arrB[b_index]
            b_index += 1
        # checks if all of b has been merged
        elif b_index >= len(arrB):
            merged_arr[i] = arrA[a_index]
            a_index += 1

        # if a is smaller than b, add to final array
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        # if b is smaller than a, add to final array
        else:
            merged_arr[i] = arrB[b_index]
            b_index += 1

    # returns the merged array
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

test_array = ['Bacon', 'Apples', 'Bears', 'Squash', 'Bananas']


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        # split up array based upon left and right
        mid = (len(arr)//2)
        left_indices = merge_sort(arr[:mid])
        right_indices = merge_sort(arr[mid:])

        arr = merge(left_indices, right_indices)
    else:
        return arr

    return arr


print(merge_sort(test_array))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
