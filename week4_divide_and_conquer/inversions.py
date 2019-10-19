# Uses python3
import sys

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions


def merge(a, b):
    c = []
    ai, bi, am, bm = 0, 0, len(a), len(b)
    i = 0
    while ai < am or bi < bm:
        if ai == am:
            c.append(b[bi])
            bi += 1
        elif bi == bm:
            c.append(a[ai])
            ai += 1
        elif a[ai] <= b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1
            i += am - ai
    # print(a, b, c, i)
    return c, i


def mergeSort(a):
    if len(a) <= 1:
        return a, 0

    m = len(a) // 2
    b, bn = mergeSort(a[:m])
    c, cn = mergeSort(a[m:])
    d, dn = merge(b, c)
    return d, bn + cn + dn


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    n = 10
    a = [1, 3, 5, 7, 9, 2, 4, 8, 10, 6]
    # b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    _, c = mergeSort(a)
    print(c)
