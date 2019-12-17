#Uses python3
import sys
import math

def sorted_x(points):
    points.sort(key=lambda p: (p[0], p[2]))
    return points

def sorted_y(points):
    return sorted(points, key=lambda p: (p[1], p[2]))

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
    for i in range(n - 1):
        for j in range(i + 1, n):
            if points[j][0] - points[i][0] >= m:
                break
            d = distance(points[i], points[j])
            if d < m:
                m = d
    return m


def split_py(py, pm, m):
    n = len(py)
    j, k = 0, 0
    lpy, rpy = [0] * m, [0] * (n - m)

    # print(py, pm)
    for i in range(n):
        if (py[i][0], py[i][2]) < (pm[0], pm[2]):
            lpy[j] = py[i]
            j += 1
        else:
            rpy[k] = py[i]
            k += 1
        # print(lpy, rpy)
        # print(m, n - m, j, k)
    return lpy, rpy


def minimum_distance(points):
    def helper(px, py, b, e):
        if e - b <= 3:
            return naive_min(px[b:e])

        m = (b + e) // 2
        lpy, rpy = split_py(py, px[m], m - b)

        d = min(helper(px, lpy, b, m), helper(px, rpy, m, e))

        return min(d, strip_min(py, d))

    px = sorted_x(points)
    py = sorted_y(points);
    # print(px)
    # print(py)
    return helper(px, py, 0, len(points))


def main():
    # input = sys.stdin.read()
    input = '11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4'
    data = list(map(int, input.split()))

    points = []
    j = 0
    for i in range(1, len(data) - 1, 2):
        points.append((data[i], data[i + 1], j))
        j += 1

    print(minimum_distance(points))


if __name__ == '__main__':
    main()
