def get_input():
    n = int(input())

    return n


def get_rectangle_cnt(n):
    dp = {1:1, 2:2, 3:3}

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n] % 10007)


if __name__=='__main__':
    n = get_input()
    get_rectangle_cnt(n=n)