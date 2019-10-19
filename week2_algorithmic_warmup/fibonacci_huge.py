# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    dp = {}
    dp[(0, 1)] = 1

    f = [0, 1]

    # print(f[-2], f[-1])

    for i in range(2, n + 1):
        f.append((f[-1] + f[-2]) % m)

        dpk = (f[-2], f[-1])

        # print(f[-2], f[-1])

        if dpk in dp:
            # print(dp)
            return get_fibonacci_huge(n % len(dp), m)

        dp[dpk] = f[-1]

    return f[-1]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, m = map(int, input().split())

    for i in range(0, 89):
        n = i
        m = 17
        print(get_fibonacci_huge_naive(n, m), get_fibonacci_huge(n, m))
