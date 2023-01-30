from copy import copy
from timeit import default_timer as timer


def timed(func):
    def wrapper_function(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        print(timer() - start)

    return wrapper_function


class Sorts:
    def __init__(self, arr) -> None:
        self.arr = copy(arr)
        self.orig_arr = copy(arr)
        self.qs_lower = 0
        self.qs_upper = len(self.arr) - 1

    def __repr__(self) -> str:
        return "Sorts[original: %s, sorted: %s]" % (self.orig_arr, self.arr)

    def reset(self):
        self.arr = copy(self.orig_arr)

    def __quicksort(self, lower, upper):

        def partition(p_lower, p_upper):
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

    def __merge_sort(self, arr):

        def merge(left, right):
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

        def heapify(arr: list, quantity: int, ini_parent: int) -> None:
            parent_idx = ini_parent
            left_idx = 2 * ini_parent + 1
            right_idx = 2 * ini_parent + 2

            if left_idx < quantity and arr[ini_parent] < arr[left_idx]:
                parent_idx = left_idx

            if right_idx < quantity and arr[parent_idx] < arr[right_idx]:
                parent_idx = right_idx

            if parent_idx != ini_parent:
                arr[ini_parent], arr[parent_idx] = arr[parent_idx], arr[ini_parent]
                heapify(arr, quantity, parent_idx)

        quantity = len(self.arr)

        for ini_parent in range(quantity, -1, -1):
            heapify(self.arr, quantity, ini_parent)

        for idx in range(quantity - 1, 0, -1):
            self.arr[idx], self.arr[0] = self.arr[0], self.arr[idx]
            heapify(self.arr, idx, 0)

    @timed
    def quicksort(self):
        self.__quicksort(self.qs_lower, self.qs_upper)

    @timed
    def merge_sort(self):
        self.arr = self.__merge_sort(self.arr)


if __name__ == '__main__':
    my_arr = [2, 3, 4, 1, 2, 7, 10, 1000, 8, 7, 1, 18, 17, 16, 15]
    sorts = Sorts(my_arr)
    sorts.heap_sort()
    print(sorts)
    sorts.reset()
    sorts.quicksort()
    print(sorts)
    sorts.reset()
    sorts.merge_sort()
    print(sorts)
