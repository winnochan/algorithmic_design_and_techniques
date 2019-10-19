# Uses python3
import sys
import itertools
import random
from pprint import pprint


def partition3_naive(A, debug=False):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3_recur(A, memo=None, s1=None, s2=None, s3=None, i=0):
    if s1 is None:
        S = sum(A)
        if S % 3 != 0:
            return 0
        s1 = s2 = s3 = S // 3
        memo = {}

    t = (0, 0, 0)
    if s1 < 0 or s2 < 0 or s3 < 0:
        return 1 if t in memo else 0

    k = tuple(sorted((s1, s2, s3)))
    if k in memo:
        return 1 if t in memo else 0

    memo[k] = i
    if i >= len(A):
        return 1 if t in memo else 0

    return partition3_recur(
        A, memo, s1 - A[i], s2, s3, i + 1) or partition3_recur(
            A, memo, s1, s2 - A[i], s3, i + 1) or partition3_recur(
                A, memo, s1, s2, s3 - A[i], i + 1)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # input = '13 1 2 3 4 5 5 7 7 8 10 12 19 25'
    # input = '3 30 30 30 30 30 30'
    # input = '10 15 18 5 21 26 24 9 8 14 4'
    # input = '10 7 10 3 10 8 10 3 1 6 8'
    # input = '10 6 7 12 16 17 17 19 21 23 27'
    # input = '10 8 2 10 10 5 6 8 8 10 8'
    # input = '10 2 6 9 9 1 10 8 9 7 8'
    # n, *A = list(map(int, input.split()))

    # print(partition3(A, 1))
    # memo = {}
    # print(partition3_recur(A, memo))
    # pprint(memo)
    # print(len(memo))
    # print(partition3_naive(A))

    # for test
    for i in range(100):
        A = [random.randint(1, 10) for _ in range(10)]
        if partition3_recur(A) != partition3_naive(A):
            print(A)
        else:
            print(i)
