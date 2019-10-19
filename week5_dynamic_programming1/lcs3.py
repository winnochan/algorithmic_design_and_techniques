#Uses python3

import sys


def lcs3(a, b, c):
    alen, blen, clen = len(a), len(b), len(c)

    dp = [[[0] * (clen + 1) for _ in range(blen + 1)] for _ in range(alen + 1)]

    for ai in range(1, alen + 1):
        for bi in range(1, blen + 1):
            for ci in range(1, clen + 1):
                if a[ai - 1] == b[bi - 1] == c[ci - 1]:
                    dp[ai][bi][ci] = max(
                        dp[ai - 1][bi - 1][ci - 1] + 1, dp[ai][bi - 1][ci - 1],
                        dp[ai - 1][bi][ci - 1], dp[ai - 1][bi - 1][ci],
                        dp[ai - 1][bi][ci], dp[ai][bi - 1][ci],
                        dp[ai][bi][ci - 1])
                else:
                    dp[ai][bi][ci] = max(
                        dp[ai - 1][bi - 1][ci - 1], dp[ai][bi - 1][ci - 1],
                        dp[ai - 1][bi][ci - 1], dp[ai - 1][bi - 1][ci],
                        dp[ai - 1][bi][ci], dp[ai][bi - 1][ci],
                        dp[ai][bi][ci - 1])

    return dp[alen][blen][clen]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # data = [3, 1, 2, 3, 3, 2, 1, 3, 3, 1, 3, 5]
    # 5 8 3 2 1 7 7 8 2 1 3 8 10 7 6 6 8 3 1 4 7
    data = [5, 8, 3, 2, 1, 7, 7, 8, 2, 1, 3, 8, 10, 7, 6, 6, 8, 3, 1, 4, 7]
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
