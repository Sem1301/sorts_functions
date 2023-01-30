import numpy as np

DEBUG = True


def heap_sort(arr) -> list:
    quantity = len(arr)

    # We loop through the array from back to front, where the initial max-heap data structure is created
    # for all the elements, because all elements are unsorted.
    # This is done with the heapify method.
    # Once this initial max-heap is formed the second for loop starts.

    for ini_parent in range(quantity, -1, -1):
        heapify(arr, quantity, ini_parent)

    # The array has max-heap structure, therefore the biggest element is located at index = 0.
    # Therefore, we swap the first element with the last element of the unsorted list, which is quantity - 1 at first.
    # After the last and the first elements have been swapped de heapify method is called again, which
    # creates the max-heap structure again for all elements except those which have already been sorted.

    for idx in range(quantity - 1, 0, -1):
        arr[idx], arr[0] = arr[0], arr[idx]
        heapify(arr, idx, 0)

    return arr


def heapify(arr: list, quantity: int, ini_parent: int) -> None:

    # Initially,
    # parent_idx is the index of the initial parent node.
    # left_idx is the index of the left child node of the initial parent node.
    # right_idx is the index of the right child node of the initial parent node.

    parent_idx = ini_parent
    left_idx = 2 * ini_parent + 1
    right_idx = 2 * ini_parent + 2

    # This if-statement checks if the parent node is less than the left child node.
    # If this is the case the index of the parent node becomes the index of the left child node.
    # The if-statement also checks if the left child even exists, by checking if left_idx is less than quantity.

    if left_idx < quantity and arr[ini_parent] < arr[left_idx]:
        parent_idx = left_idx

    # The same if-statement for the right child node, but because the initial parent might have been replaced by
    # the left_child node, we input parent_idx instead of ini_parent.
    # The index of the new parent becomes the index of the right child node if this if-statement is true.

    if right_idx < quantity and arr[parent_idx] < arr[right_idx]:
        parent_idx = right_idx

    # This if-statement checks if the index of the parent node has changed.
    # If so the initial parent node is swapped with the new the left or right child not, depending on which is largest.
    # Then the function calls itself with the new parent as the initial parent.

    if parent_idx != ini_parent:
        arr[ini_parent], arr[parent_idx] = arr[parent_idx], arr[ini_parent]
        heapify(arr, quantity, parent_idx)


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
        print('Your sorted list:')
        print(heap_sort(np.array(arr)))


if __name__ == '__main__':
    main()
