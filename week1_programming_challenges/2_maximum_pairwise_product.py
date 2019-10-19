#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest

from typing import List


# calculate all results and store the maximum result
# O(n ^ 2)
def naive(a: List[int]) -> int:
    maximum: int = 0

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue

            result: int = a[i] * a[j]
            if result > maximum:
                maximum = result

    return maximum


# O(n * log(n))
def fast_by_sort(a: List[int]) -> int:
    a = sorted(a)
    return a[-1] * a[-2]


# O(2 * n)
def fast_wrong(a: List[int]) -> int:
    ai: int = 0
    aj: int = 0

    for n in a:
        if n > ai:
            ai = n

    for n in a:
        if n > aj and n < ai:
            aj = n

    return ai * aj


# O(2 * n)
def fast_right(a: List[int]) -> int:
    m = -1
    ai = 0
    aj = 0
    for i in range(len(a)):
        if a[i] > ai:
            ai = a[i]
            m = i

    for j in range(len(a)):
        if a[j] == ai and j == m:
            continue
        elif a[j] == ai and j != m:
            aj = a[j]
            # it can break at this step
        elif a[j] > aj:
            aj = a[j]

    return ai * aj


class TestFastSolutions(unittest.TestCase):
    def gen_test_data(self):
        n: int = random.randint(2, 200000)
        return [random.randint(0, 200000) for _ in range(n)]

    # def test_fast_by_sort(self):
    #     for _ in range(100):
    #         td = self.gen_test_data()
    #         self.assertEqual(naive(td), fast_by_sort(td), msg=td)

    # def test_fast_wrong(self):
    #     for _ in range(10000):
    #         td = self.gen_test_data()
    #         self.assertEqual(naive(td), fast_wrong(td), msg=td)

    def test_fast_right(self):
        for _ in range(100):
            td = self.gen_test_data()
            self.assertEqual(naive(td), fast_right(td), msg=td)


unittest.main()
