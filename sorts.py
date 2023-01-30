import re
from copy import copy
from timeit import default_timer as timer

DEBUG = True


def timed(func):
    def wrapper_function(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        print("Timed:", timer() - start)

    return wrapper_function


class Sorts(object):
    def __init__(self, arr: list) -> None:
        self.arr: list = copy(arr)
        self.orig_arr: list = copy(arr)
        self.qs_lower: int = 0
        self.qs_upper: int = len(self.arr) - 1

    def __repr__(self) -> str:
        return "Sorts[original: %s, sorted: %s]" % (self.orig_arr, self.arr)

    def reset(self) -> None:
        self.arr = copy(self.orig_arr)

    def __quicksort(self, lower: int, upper: int) -> None:

        def partition(p_lower: int, p_upper: int) -> int:
            pivot = self.arr[p_upper]
            n = p_lower - 1

            for k in range(p_lower, p_upper):
                if self.arr[k] <= pivot:
                    n += 1
                    self.arr[n], self.arr[k] = self.arr[k], self.arr[n]

            self.arr[n + 1], self.arr[p_upper] = self.arr[p_upper], self.arr[n + 1]

            return n + 1

        if lower < upper:
            pivot_num = partition(lower, upper)
            self.__quicksort(lower, pivot_num - 1)
            self.__quicksort(pivot_num + 1, upper)

    def __merge_sort(self, arr: list) -> list:

        def merge(left: list, right: list) -> list:
            sorted_arr = []
            left_idx, right_idx = 0, 0
            length_left, length_right = len(left), len(right)

            while left_idx < length_left and right_idx < length_right:
                if left[left_idx] <= right[right_idx]:
                    sorted_arr.append(left[left_idx])
                    left_idx += 1
                else:
                    sorted_arr.append(right[right_idx])
                    right_idx += 1

            while left_idx < length_left:
                sorted_arr.append(left[left_idx])
                left_idx += 1

            while right_idx < length_right:
                sorted_arr.append(right[right_idx])
                right_idx += 1

            return sorted_arr

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        left_arr = self.__merge_sort(left_arr)
        right_arr = self.__merge_sort(right_arr)

        return merge(left_arr, right_arr)

    @timed
    def heap_sort(self) -> None:

        def heapify(arr: list, h_quantity: int, h_ini_parent: int) -> None:
            parent_idx = h_ini_parent
            left_idx = 2 * h_ini_parent + 1
            right_idx = 2 * h_ini_parent + 2

            if left_idx < h_quantity and arr[h_ini_parent] < arr[left_idx]:
                parent_idx = left_idx

            if right_idx < h_quantity and arr[parent_idx] < arr[right_idx]:
                parent_idx = right_idx

            if parent_idx != h_ini_parent:
                arr[h_ini_parent], arr[parent_idx] = arr[parent_idx], arr[h_ini_parent]
                heapify(arr, h_quantity, parent_idx)

        quantity = len(self.arr)

        for ini_parent in range(quantity, -1, -1):
            heapify(self.arr, quantity, ini_parent)

        for idx in range(quantity - 1, 0, -1):
            self.arr[idx], self.arr[0] = self.arr[0], self.arr[idx]
            heapify(self.arr, idx, 0)

    @timed
    def quicksort(self) -> None:
        self.__quicksort(self.qs_lower, self.qs_upper)

    @timed
    def merge_sort(self) -> None:
        self.arr = self.__merge_sort(self.arr)

    @timed
    def insertion_sort(self) -> None:
        quantity = len(self.arr)

        for idx in range(1, quantity):
            predecessor_idx = idx - 1
            key = self.arr[idx]

            while predecessor_idx >= 0 and key < self.arr[predecessor_idx]:
                self.arr[predecessor_idx + 1] = self.arr[predecessor_idx]
                predecessor_idx -= 1

            self.arr[predecessor_idx + 1] = key


def validate_input(value: str) -> list:
    items = re.split(r"[,;\s]+", value)
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
        sorts = Sorts(arr)
        print("Heap sort")
        sorts.heap_sort()
        print(sorts)
        print("Quick sort")
        sorts.reset()
        sorts.quicksort()
        print(sorts)
        print("Merge sort")
        sorts.reset()
        sorts.merge_sort()
        print(sorts)
        print("Insertion sort")
        sorts.reset()
        sorts.insertion_sort()
        print(sorts)


if __name__ == '__main__':
    main()
