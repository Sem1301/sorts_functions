import numpy as np

DEBUG = True


def merge_sort(arr):

    # We check for if the sub-arrays are empty or contain one element.

    if len(arr) <= 1:
        return arr

    # Here the array or sub-array gets divided into its left and right halves.

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Here the function is called upon itself with the left and right sub-arrays, also dividing them.
    # This is done until the sub-arrays contain 0 or 1 elements.

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # we return de merge function on the left and right sub-arrays which will execute the comparing and sorting.

    return merge(left_arr, right_arr)


def merge(left, right):

    sorted_arr = []

    # we set two index pointers to zero

    left_idx, right_idx = 0, 0

    # we are checking for all indexes in the sub-arrays, so we define two
    # variables that represent the length of the sub-arrays

    length_left, length_right = len(left), len(right)

    # If the left or right index is greater than the length of the corresponding sub-array
    # we have checked for all elements, so that explains the while loop.

    while left_idx < length_left and right_idx < length_right:

        # We check whether the element in the left half at the index left_idx is less than or equal to
        # the element in the right half at the index right_idx
        # If so we append that element to our sorted array
        # Else we append the right element at the index right_idx, since that happens to be the lesser element
        # Depending on which element got appended to the sorted array we shift that index by one
        # and check again if the while loop is still true

        if left[left_idx] <= right[right_idx]:
            sorted_arr.append(left[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1

    # If the previous while loop is false it checks if left_idx is still less than the length of the left half
    # while that is true it appends the left-over elements from the left sub-array to the sorted array
    # It does the same for the right half

    while left_idx < length_left:
        sorted_arr.append(left[left_idx])
        left_idx += 1
    while right_idx < length_right:
        sorted_arr.append(right[right_idx])
        right_idx += 1

    # It returns a python list and not a numpy array
    # This is the case because we used an empty list as a container and return that list once every element has
    # been appended, so we only convert back to a python list in the last step
    # which means that any optimization as a consequence of using numpy has not been lost

    return sorted_arr


def validate_input(value: str) -> list:
    items = value.split(' ')
    ret = []
    for item in items:
        try:
            ret.append(int(item))
        except ValueError:
            if DEBUG:
                print("Invalid value [{}] ignoring...".format(item))
    return ret


def main():
    while True:
        input_arr = input('input your list, separate the elements of the list with spaces: ')
        if input_arr == 'stop':
            break
        arr = validate_input(input_arr)
        print('your sorted array: ')
        print(merge_sort(np.array(arr)))


if __name__ == '__main__':
    merge_sort([1, 5, 4, 3, 8])
    main()
