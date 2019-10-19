# Uses python3
import re
from pprint import pprint


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(num_list, op_list):
    n = len(num_list)
    max_value = [[0] * n for _ in range(n)]
    min_value = [[0] * n for _ in range(n)]

    # print(num_list, op_list)

    for i in range(n):
        max_value[i][i] = num_list[i]
        min_value[i][i] = num_list[i]

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            M, m = float('-inf'), float('inf')
            for k in range(i, j):
                a = evalt(max_value[i][k], max_value[k + 1][j], op_list[k])
                b = evalt(max_value[i][k], min_value[k + 1][j], op_list[k])
                c = evalt(min_value[i][k], max_value[k + 1][j], op_list[k])
                d = evalt(min_value[i][k], min_value[k + 1][j], op_list[k])

                M = max(M, a, b, c, d)
                m = min(m, a, b, c, d)

            max_value[i][j] = M
            min_value[i][j] = m

    # pprint(min_value, width=40)
    # pprint(max_value, width=40)

    return max_value[0][n - 1]


if __name__ == "__main__":
    # expr = input()
    expr = '5-8+7*4-8+9'
    op_list = [c for c in expr if c in '-+*']
    num_list = list(map(int, re.sub(r'[\+\-\*]', ' ', expr).split(' ')))
    print(get_maximum_value(num_list, op_list))
