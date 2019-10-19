# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1


def get_majority_element_o_n(a):
    c = {}
    n = len(a)
    h = n // 2 + 1
    for i in a:
        c.setdefault(i, 0)
        c[i] += 1
        if c[i] >= h:
            return i
    return -1


if __name__ == '__main__':
    # | 9 3 | 9 9 | 2 9 | 2 2 | 9
    print(get_majority_element_o_n([9, 3, 9, 9, 2, 9, 2, 2, 9]))
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
