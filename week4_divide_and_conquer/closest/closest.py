#Uses python3
import sys
import math
import random
import unittest


def cmp_by_x(self, other):
    if self.x < other.x:
        return -1
    elif self.x == other.x and self.y < other.y:
        return -1
    elif self.x == other.x and self.y == other.y:
        return 0
    else:
        return 1


def cmp_by_y(self, other):
    if self.y < other.y:
        return -1
    elif self.y == other.y and self.x < other.x:
        return -1
    elif self.y == other.y and self.x == other.x:
        return 0
    else:
        return 1


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str((self.x, self.y))

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def sorted_x(points):
    return sorted(points, key=cmp_to_key(cmp_by_x))


def sorted_y(points):
    return sorted(points, key=cmp_to_key(cmp_by_y))


def naive_min(points):
    n = len(points)
    m = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            m = min(m, points[i].distance(points[j]))
    return m


def strip_min(points, m):
    n = len(points)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if points[j].y - points[i].y >= m:
                break
            m = min(m, points[i].distance(points[j]))
    return m


def split_px(px):
    m = len(px) // 2
    return px[:m], px[m:]


def split_py(px, py):
    n = len(py)
    m = n // 2
    j, k = 0, 0
    lpy, rpy = [0] * m, [0] * (n - m)
    for i in range(n):
        if cmp_by_x(py[i], px[m]) < 0:
            lpy[j] = py[i]
            j += 1
        else:
            rpy[k] = py[i]
            k += 1
    return lpy, rpy


def minimum_distance(points):
    pmap = {}
    for i in range(len(points)):
        if (points[i].x, points[i].y) in pmap:
            return .0
        pmap[(points[i].x, points[i].y)] = True

    def helper(px, py):
        if len(px) <= 3:
            return naive_min(px)

        lpx, rpx = split_px(px)
        lpy, rpy = split_py(px, py)

        d = min(helper(lpx, lpy), helper(rpx, rpy))

        return min(d, strip_min(py, d))

    return helper(sorted_x(points), sorted_y(points))


def gen_test_data(n):
    m = 1000000000
    return [
        Point(random.randint(-m, m), random.randint(-m, m)) for i in range(n)
    ]


# class TestMinimumDistance(unittest.TestCase):
#     def test_minimum_distance(self):
#         for _ in range(2000):
#             arr = gen_test_data(20)
#             self.assertEqual(minimum_distance(arr), naive_min(arr), msg=arr)
#         return

#     def test_time(self):
#         arr = gen_test_data(1000)
#         # self.assertEqual(naive_min(arr), naive_min(arr), msg=arr)
#         self.assertEqual(minimum_distance(arr), minimum_distance(arr), msg=arr)


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    points = []
    for i in range(1, len(data) - 1, 2):
        points.append(Point(data[i], data[i + 1]))

    # points = gen_test_data(200000)

    print(minimum_distance(points))


if __name__ == '__main__':
    main()
    # unittest.main()
