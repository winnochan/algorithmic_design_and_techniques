# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments.sort(key=lambda s: s.end)

    l = None
    for s in segments:
        if not l or s.start > l.end:
            l = s
            points.append(s.end)

    return points


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *data = map(int, input.split())
    n, *data = 3, 1, 3, 2, 5, 3, 6
    # n, *data = 4, 4, 7, 1, 3, 2, 5, 5, 6
    segments = list(
        map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
