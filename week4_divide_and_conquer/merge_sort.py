#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


a = [1, 3, 5, 7, 9, 2, 4, 8, 10, 6]
print(mergeSort(a))
