#Uses python3
import sys
import math

def radix_sort(points, index):
    c = [[] for _ in range(19)]

    n = len(points)
    p = points[:]
    # p = points
    for i in range(1, 11):
        for j in range(n):
            b = (abs(p[j][index]) // i) % 10
            if p[j][index] < 0:
                b = -b
            c[b + 9].append(p[j])

        t = 0
        for b in range(19):
            for k in range(len(c[b])):
                p[t] = c[b][k]
                t += 1
            c[b] = []

    # print('radix', index, p)
    return p

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def naive_min(points):
    n = len(points)
    m = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < m:
                m = d
    return m


def strip_min(points, m):
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            if points[j][0] - points[i][0] >= m:
                break
            d = distance(points[i], points[j])
            if d < m:
                m = d
    # print('strip', m)
    return m

def minimum_distance(points):
    def helper(points, b, e):
        if e - b <= 3:
            return naive_min(points[b:e])

        m = (b + e) // 2
        d = min(helper(points, b, m), helper(points, m, e))

        # print('d', d)
        return min(d, strip_min(radix_sort(points[b:e], 1), d))

    return helper(radix_sort(points, 0), 0, len(points))

def main():
    # input = '11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4'
    input = '10 -85 -46 -2 -36 -39 95 56 -88 95 -54 50 -18 32 -100 -63 -69 -40 -32 37 11'
    data = list(map(int, input.split()))

    points = []
    for i in range(1, len(data) - 1, 2):
        points.append((data[i], data[i + 1]))

    # print(radix_sort(points, 0))
    # print(radix_sort(points, 1))
    print(minimum_distance(points))
    # print(naive_min(points))

if __name__ == '__main__':
    main()
