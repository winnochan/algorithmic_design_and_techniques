# Uses python3
import sys


def get_change(m):
    #write your code here
    t = 0
    t += m // 10
    m %= 10
    t += m // 5
    m %= 5
    t += m
    return t


if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = 28
    print(get_change(m))
