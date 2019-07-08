# coding utf-8


def quick_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    else:
        pivot =  alist[0]
        greater = [i for i in alist[1:] if i >pivot]
        lesser = [i for i in alist[1:] if i <= pivot]
        return quick_sort(lesser) + [pivot]