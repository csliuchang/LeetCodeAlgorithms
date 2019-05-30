# coding utf -8
from __future__ import print_function


def select_sort(alist):
    """ 选择排序 """
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist


if __name__ == '__main__':
    try:
        raw_input  # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(select_sort(unsorted))

