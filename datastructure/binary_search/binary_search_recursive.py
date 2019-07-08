# coding utf-8


def binary_search(alist, item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        print(mid)
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


if __name__ == "__main__":
    li = (12, 34, 45, 67, 78, 96)
    print(binary_search(li, 34))