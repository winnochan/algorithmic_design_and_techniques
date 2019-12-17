import random
import unittest

import closest
import radix_closest


def gen_test_data(n):
    # m = 1000000000
    m = 1000
    return [(random.randint(-m, m), random.randint(-m, m), i) for i in range(n)]


# points = gen_test_data(200000)
class TestMinimumDistance(unittest.TestCase):
    def test_minimum_distance(self):
        for _ in range(3000):
            arr = gen_test_data(10)
            self.assertEqual(closest.minimum_distance(arr[:]),
                             closest.naive_min(arr[:]),
                             msg=str(arr))
        return

    # def test_time(self):
    #     arr = gen_test_data(1000)
    #     self.assertEqual(closest.minimum_distance(arr),
    #                      closest.minimum_distance(arr),
    #                      msg=arr)
    #     return

    # def test_sort(self):
    #     self.assertEqual(closest.radix_sort(points),
    #                      closest.radix_sort(points))



def main():
    points = gen_test_data(100000)
    # print(points)
    # print(closest.minimum_distance(points))
    print(radix_closest.minimum_distance(points))
    # print(closest.radix_sort(points, 0, 10))

    # closest.sorted_x(points)
    # closest.sorted_y(points)
    # mergeSort(points, closest.cmp_by_x)
    # mergeSort(points, closest.cmp_by_y)

    # px, py = closest.radix_sort(points)
    # closest.radix_sort(points, 0, 10)
    # closest.radix_sort(points, 1, 10)
    print('sorted done')


if __name__ == '__main__':
    # main()
    unittest.main()
