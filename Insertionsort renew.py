import numpy as np

DEBUG = True


def insertion_sort(arr):

    quantity = len(arr)

    # Here we loop through all indexes of the array

    for idx in range(1, quantity):

        # We define a variable which is the index of the predecessor of arr[idx]
        # We define another variable, key, which is the element at index idx

        predec_idx = idx - 1
        key = arr[idx]

        # This while loop stays true if the predecessor is smaller than the key we are looking at
        # while the loop is true, the predecessor gets swapped with the next element in the array
        # The index of the predecessor is now one element to the left, since the key is now swapped with its
        # predecessor
        # If the index of the predecessor is less than zero we have checked for all elements before the key-element
        # thus the while loop ends, and we check for the next key-element

        while predec_idx >= 0 and key < arr[predec_idx]:
            arr[predec_idx + 1] = arr[predec_idx]
            predec_idx -= 1

        # Here we change our key back to what it was originally, because we didn't swap, but changed the value

        arr[predec_idx + 1] = key

    print('your sorted list: ')
    print(arr)
    return arr


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


def main() -> None:
    while True:
        input_arr = input('input your list, separate the elements of the list with spaces: ')
        if input_arr == 'stop':
            break
        arr = validate_input(input_arr)
        insertion_sort(np.array(arr))


if __name__ == '__main__':
    main()
