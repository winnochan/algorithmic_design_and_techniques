# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum(n):
    if n <= 1:
        return n

    if n >= 60:
        return fibonacci_sum(n % 60)

    s = [
        0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4,
        2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8,
        4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0
    ]
    return s[n]


def fibonacci_sequence(n):
    if n <= 0:
        return [0]

    if n <= 1:
        return [0, 1]

    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f


def fibonacci_sequence_mod10(n):
    if n <= 0:
        return [0]

    if n <= 1:
        return [0, 1]

    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10

    return f


def fibonacci_sequence_sum(n):
    if n <= 0:
        return [0]

    if n <= 1:
        return [0, 1]

    f = [0] * (n + 1)
    s = [0] * (n + 1)
    f[1] = 1
    s[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2])
        s[i] = s[i - 1] + f[i]

    return s


def fibonacci_sequence_sum_mod10(n):
    if n <= 0:
        return [0]

    if n <= 1:
        return [0, 1]

    f = [0] * (n + 1)
    s = [0] * (n + 1)
    f[1] = 1
    s[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10
        s[i] = (s[i - 1] + f[i]) % 10
    return s


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input())
    # print(fibonacci_sum_naive(n))
    # print(fibonacci_sequence(59))
    print(fibonacci_sequence_mod10(59))
    # print(fibonacci_sequence_sum(59))
    print(fibonacci_sequence_sum_mod10(59))

    # for i in range(100):
    #     print(fibonacci_sum_naive(i), fibonacci_sum(i))
