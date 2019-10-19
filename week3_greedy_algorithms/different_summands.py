# Uses python3
import sys


def optimal_summands(n):
    n -= 1
    summands = [1]
    while n > 0:
        if n > summands[-1]:
            summands.append(summands[-1] + 1)
            n -= summands[-1]
        else:
            summands[-1] += n
            n = 0
    return summands


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    n = 7
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
