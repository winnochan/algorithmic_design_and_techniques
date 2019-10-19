#Uses python3

import sys
from pprint import pprint


def lcs2(a, b):
    """
    if a[j] == b[k]:
        DP(j, k) = max(DP(j - 1, k - 1) + 1, DP(j, k - 1), DP(j - 1, k))
    else:
        DP(j, k) = max(DP(j - 1, k - 1), DP(j, k - 1), DP(j - 1, k))
    """

    la, lb = len(a), len(b)
    dp = [[0] * (lb + 1) for _ in range(la + 1)]

    for j in range(1, la + 1):
        for k in range(1, lb + 1):
            if a[j - 1] == b[k - 1]:
                dp[j][k] = max(dp[j - 1][k - 1] + 1, dp[j][k - 1],
                               dp[j - 1][k])
            else:
                dp[j][k] = max(dp[j - 1][k - 1], dp[j][k - 1], dp[j - 1][k])

    # pprint(dp)

    return dp[la][lb]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))

    data = [3, 2, 7, 5, 2, 2, 5]
    data = [1, 7, 4, 1, 2, 3, 4]
    data = [4, 2, 7, 8, 3, 5, 2, 8, 7]

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
