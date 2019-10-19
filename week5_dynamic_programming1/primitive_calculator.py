# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def dp_sequence(n):
    dp = (n + 1) * [0]

    dp[1] = 1

    for i in range(1, n):
        for t in [i + 1, i * 2, i * 3]:
            if t <= n:
                if not dp[t] or dp[i] + 1 < dp[t]:
                    dp[t] = dp[i] + 1

    s = [n]
    for i in range(dp[s[-1]], 1, -1):
        if s[-1] % 6 == 0:
            for t in [s[-1] // 3, s[-1] // 2, s[-1] - 1]:
                if dp[t] == i - 1:
                    s.append(t)
                    break
        elif s[-1] % 3 == 0:
            for t in [s[-1] // 3, s[-1] - 1]:
                if dp[t] == i - 1:
                    s.append(t)
                    break
        elif s[-1] % 2 == 0:
            for t in [s[-1] // 2, s[-1] - 1]:
                if dp[t] == i - 1:
                    s.append(t)
                    break
        else:
            s.append(s[-1] - 1)

    return s[::-1]


# input = sys.stdin.read()
# n = int(input)
n = 1
# n = 100
n = 96234
sequence = list(dp_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
