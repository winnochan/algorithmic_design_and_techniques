# Uses python3
import sys


def binary_search(points, num, left=0, right=None):
    if right is None:
        right = len(points) - 1

    # print('binary search', points, left, right)
    if left >= right:
        return left if points[left][1] >= num else left + 1

    mid = (left + right) // 2
    if points[mid][1] == num:
        return mid
    elif points[mid][1] > num:
        return binary_search(points, num, left, mid - 1)
    else:
        return binary_search(points, num, mid + 1, right)


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    points = [(i, points[i]) for i in range(len(points))]
    points.sort(key=lambda p: p[1])
    for i in range(len(starts)):
        s = starts[i]
        e = ends[i]

        si = binary_search(points, s)
        ei = binary_search(points, e)
        # print(points, s, e, si, ei)
        if si < ei:
            cnt[points[si][0]] += 1
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # data = [2, 3, 0, 5, 7, 10, 1, 6, 11]
    # data = [1, 3, -10, 10, -100, 100, 0]
    data = [3, 2, 0, 5, -3, 2, 7, 10, 1, 6]
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
