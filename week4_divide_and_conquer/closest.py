#Uses python3
import sys
import math
import random
import unittest


def sorted_x(points):
    return sorted(points, key=lambda p: p[0])


def sorted_y(points):
    return sorted(points, key=lambda p: p[1])


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force(points):
    n = len(points)
    m = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < m:
                m = d
    return m


def minimum_distance(points):
    def helper(px, py):
        n = len(px)

        if n <= 1:
            return float('inf')

        if n == 2:
            return distance(px[0], px[1])

        m = n // 2
        lpx, rpx, lpy, rpy = px[:m], px[m:], [], []

        for i in range(n):
            if py[i][0] < px[m][0]:
                lpy.append(py[i])
            else:
                rpy.append(py[i])

        d = min(helper(lpx, lpy), helper(rpx, rpy))

        dpy = [py[i] for i in range(n) if py[i][0] - py[m][0] < d]
        return min(d, brute_force(dpy))

    return helper(sorted_x(points), sorted_y(points))


class TestMinimumDistance(unittest.TestCase):
    def gen_test_data(self, n):
        m = 1000000000
        return [(random.randint(-m, m), random.randint(-m, m))
                for i in range(n)]

    def test_minimum_distance(self):
        for i in range(1000):
            arr = self.gen_test_data(100)
            self.assertEqual(minimum_distance(arr), brute_force(arr), msg=arr)
        return


def main():
    input = sys.stdin.read()
    # input = '2 0 0 3 4'
    # input = '4 7 7 1 100 4 8 7 7'
    # input = '11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4'
    data = list(map(int, input.split()))

    n = data[0]
    points = []
    pmap = {}
    for i in range(1, len(data) - 1, 2):
        p = (data[i], data[i + 1])
        if p in pmap:
            print(.0)
            return
        points.append(p)

    # print(minimum_distance(points))
    print("{0:.4f}".format(minimum_distance(points)))


if __name__ == '__main__':
    # main()
    unittest.main()
