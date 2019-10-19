# Uses python3
import sys
import random


def partition3(a, l, r):
    pivot = a[l]
    ltidx = l - 1
    eqidx = l

    # print('init', pivot, ltidx, eqidx, a)
    for gtidx in range(l + 1, r + 1):
        if a[gtidx] == pivot:
            eqidx += 1
            if eqidx != gtidx:
                a[eqidx], a[gtidx] = a[gtidx], a[eqidx]
            # print('equal', pivot, ltidx, eqidx, gtidx, a)
        elif a[gtidx] < pivot:
            ltidx += 1
            eqidx += 1
            if eqidx == gtidx:
                a[ltidx], a[eqidx] = a[eqidx], a[ltidx]
                # a[ltidx], a[gtidx] = a[gtidx], a[ltidx]
            else:
                a[ltidx], a[eqidx], a[gtidx] = a[gtidx], a[ltidx], a[eqidx]
            # print('lest', pivot, ltidx, eqidx, gtidx, a)

    # print('final', pivot, ltidx, eqidx, a)
    return (ltidx, eqidx + 1)


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    m1, m2 = partition3(a, l, r)
    randomized_quick_sort3(a, l, m1)
    randomized_quick_sort3(a, m2, r)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    a = [random.randint(1, 5) for _ in range(10)]
    n = len(a)
    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
