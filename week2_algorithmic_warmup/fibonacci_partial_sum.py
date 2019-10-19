# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum(src, dst):
    f = [
        0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7,
        8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3,
        6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1
    ]

    s = [
        0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4,
        2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8,
        4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0
    ]
    return (s[dst % 60] - s[(src - 1) % 60]) % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    # from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))

    for i in range(100):
        print(fibonacci_partial_sum_naive(i, i + 10),
              fibonacci_partial_sum(i, i + 10))
