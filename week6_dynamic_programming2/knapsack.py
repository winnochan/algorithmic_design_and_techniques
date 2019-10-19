# Uses python3
import sys
from pprint import pprint


def optimal_weight(W, w):
    """
    knapsack without repetitions

    definition: use at most n items to calculate the max weight which does not exceed w

    dp(w, i) = max{ dp(w - w[i], i - 1) + w[i], dp(w, i - 1) }
    """

    dp = [[0] * (W + 1) for _ in range(len(w) + 1)]

    for i in range(1, len(w) + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j]

            if j >= w[i - 1]:
                v = dp[i - 1][j - w[i - 1]] + w[i - 1]
                if v > dp[i][j]:
                    dp[i][j] = v

    # pprint(dp)

    return dp[len(w)][W]


if __name__ == '__main__':
    # input = sys.stdin.read()
    input = '10 3 1 4 8'
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
