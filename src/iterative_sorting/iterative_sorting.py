arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # Loops through the array again and checks for the
        # smallest index. If the current index is greater than the smaller
        # index. sets the new smaller index of the index of the array
        for j in range(smallest_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Because the current index is set when it starts to iterate
        # We want to swap the smallest with the current
        arr[cur_index], arr[smallest_index] = \
            arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    array_length = len(arr)

    # loops through the aray
    for i in range(array_length):
        # Creates another loop that will compare the two indexes
        # of i and j and returns them in order from small to large
        for j in range(array_length - 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bubble_sort(arr1))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
