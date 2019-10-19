# Uses python3
import sys


def get_change(m):
    dp = [0] * (m + 1)

    for i in range(m):
        for t in [i + 1, i + 3, i + 4]:
            if t <= m:
                if not dp[t]:
                    dp[t] = dp[i] + 1
                elif dp[i] + 1 < dp[t]:
                    dp[t] = dp[i] + 1

    # print(dp)
    return dp[m]


def get_change_recursive(m, c={}):
    if m <= 0:
        return 0
    if m in c:
        return c[m]

    c[m] = min(get_change_recursive(m - 1, c), get_change_recursive(m - 3, c),
               get_change_recursive(m - 4, c)) + 1
    return c[m]


if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = 137
    print(get_change(m))
    print(get_change_recursive(m))
