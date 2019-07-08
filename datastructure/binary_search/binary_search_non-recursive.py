# coding utf-8


def binary_search(alist, item):
    """
    binary search using non-recursive
    Optimal time complexity o(1)
    the worst time comlexity o(log n)
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False
