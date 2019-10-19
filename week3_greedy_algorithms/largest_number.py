#Uses python3

import sys
import unittest
import random
from itertools import permutations
from functools import cmp_to_key


def largest_number_naive(a):
    l = 0
    for s in permutations(a):
        n = int(''.join(s))
        if n > l:
            l = n
    return str(l)


def largest_number(a):
    a.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
    return ''.join(a)


class TestLargestNumber(unittest.TestCase):
    def get_test_data(self):
        # n = random.randint(10, 20)
        return [str(random.randint(1, 20)) for _ in range(7)]

    def test_largest_number(self):
        for _ in range(1000):
            a = self.get_test_data()
            self.assertEqual(largest_number_naive(a), largest_number(a), msg=a)

        self.assertEqual(largest_number_naive(['21', '2']),
                         largest_number(['21', '2']))


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = input.split()
    # data = [5, 958, 4, 985]
    # a = list(map(str, data[1:]))
    # print(largest_number(a))
    # print(largest_number_naive(a))
    unittest.main()
