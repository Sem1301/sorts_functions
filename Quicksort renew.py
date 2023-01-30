import random
import numpy as np


def quicksort(arr):

    if order(arr):
        return arr

    else:
        quantity = len(arr)
        random_idx = random.randrange(0, quantity)
        rot_point = arr[random_idx]
        left = []
        right = []

        for num in arr:
            if num > rot_point:
                right.append(num)
            else:
                left.append(num)

        left = quicksort(left)
        right = quicksort(right)

        for num in right:
            left.append(num)

        return left


def order(arr):

    switch = False
    i = 1

    while i < len(arr):
        if arr[i] < arr[i - 1]:
            switch = True
        else:
            switch = False
        i += 1

    return switch


def main():
    quicksort([1, 2, 3, 4, 5])


if __name__ == '__main__':
    main()
