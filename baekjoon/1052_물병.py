import sys

def get_input():
    n, k = map(int, sys.stdin.readline().split())

    return n, k

def get_count(n, k):
    buy_cnt = 0

    while bin(n).count('1') > k:

        n += 1
        buy_cnt += 1

    print(buy_cnt)

if __name__ == '__main__':
    n, k = get_input()
    get_count(n=n, k=k)
