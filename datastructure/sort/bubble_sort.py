# coding : utf-8
from __future__ import print_function


def bubble_sort(alist):
    """ bubble sort """
    for j in range(len(alist) - 1):
        count = 0
        for i in range(0, len(alist) - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:  # 改进之后最优时间复杂度为 0（n）最坏不变为0（n^2）
            break
    return alist


if __name__ == '__main__':
    try:
        raw_input  # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))
