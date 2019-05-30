from __future__ import print_function


def insertion_sort(alist):
    """
    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2]
    [0, 2, 2, 3, 5]
    >>> insertion_sort([])
    []
    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    看了MIT的教程对代码项目有很多感悟，写代码也要有一种仪式感，仅仅是运行是不够的，一点是别人能看，另外一点是别人方便直观的看
    后期准备在代码加入time程序直观反映各算法计算时间。
    """
    # for index in range(1, len(collection)):
    #     while index > 0 and collection[index - 1] > collection[index]:
    #         collection[index], collection[index - 1] = collection[index - 1], collection[index]
    #         index -= 1
    #
    # return collection
    for j in range(1, len(alist)):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break
    return alist


if __name__ == '__main__':
    try:
        raw_input  # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))

