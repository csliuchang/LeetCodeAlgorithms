# coding utf -8
def select_sort(alist):
    """ 选择排序 """
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    l1 = [23, 4, 56, 7, 8, 8, 53, 4, 65, 7, 8, 9, 0, 4, 55, 6, 7, 8, 99]
    print(l1)
    select_sort(l1)
    print(l1)

