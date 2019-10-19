# Uses python3

from pprint import pprint


def edit_distance(s, t):
    """
    if s[j - 1] == t[k - 1]:
        DP(j, k) = min(DP(j - 1, k - 1), DP(j, k - 1) + 1, DP(j - 1, k) + 1)
    else:
        DP(j, k) = min(DP(j - 1, k - 1), DP(j, k - 1), DP(j - 1, k)) + 1
    """

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for k in range(len(t) + 1):
        dp[0][k] = k
    for j in range(len(s) + 1):
        dp[j][0] = j

    for j in range(1, len(s) + 1):
        for k in range(1, len(t) + 1):
            if s[j - 1] == t[k - 1]:
                dp[j][k] = min(dp[j - 1][k - 1], dp[j][k - 1] + 1,
                               dp[j - 1][k] + 1)
            else:
                dp[j][k] = min(dp[j - 1][k - 1] + 1, dp[j][k - 1] + 1,
                               dp[j - 1][k] + 1)
    # pprint(dp)

    #write your code here
    return dp[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance("editing", "distance"))
    # print(edit_distance(input(), input()))
