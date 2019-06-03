# coding: utf-8
from __future__ import print_function


def shell_sort(alist):   # sort is unstable  to prepare modity
    """ 希尔排序 """
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[1 - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


if __name__ == '__main__':
    try:
        raw_input  # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(shell_sort(unsorted))

