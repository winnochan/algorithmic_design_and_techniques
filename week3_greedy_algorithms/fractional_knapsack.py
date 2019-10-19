# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    vw = [(values[i], weights[i]) for i in range(len(weights))]

    vw.sort(key=lambda t: t[0] / t[1], reverse=True)

    print(vw)

    for i in range(len(vw)):
        if capacity <= 0:
            break

        v, w = vw[i]

        if w <= capacity:
            capacity -= w
            value += v
        else:
            value += (v / w) * capacity
            capacity = 0

    return value


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # 3 50 60 20 100 50 120 30
    data = [3, 50, 60, 20, 100, 50, 120, 30]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
