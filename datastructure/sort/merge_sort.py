# coding utf-8


def merge_sort(alist):
    """ merge sort """

    n = len(alist)
    if n <= 1 :
        return alist
    mid = n//2

    # a new left list by using merge sort
    left_li = merge_sort(alist[:mid])

    # a new right list by using merge sort
    right_li = merge_sort(alist[mid:])

    """
    merge two order list as one new list
    """

    # setting two points
    left_pointer,right_pointer = 0, 0

    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    li=[35,56,78,34,28,98,78,68,56,49]
    print(li)
    sorted_li=merge_sort(li)
    print(sorted_li)