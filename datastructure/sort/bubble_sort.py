# coding : utf-8
def bubble_sort(alist):
    """ bubble sort """
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:  # 改进之后最优时间复杂度为 0（n）最坏不变为0（n^2）
            return


if __name__ == "__main__":
    l1 = [23, 4, 56, 7, 8, 8, 53, 4, 65, 7, 8, 9, 0, 4, 55, 6, 7, 8, 99]
    print(l1)
    bubble_sort(l1)
    print(l1)
