def get_input():
    numeric = int(input())

    return numeric


def get_min_calculate_cnt(numeric):
    dp = [0] * (numeric + 1)

    for i in range(2, numeric + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[numeric])


if __name__ == '__main__':
    numeric = get_input()
    get_min_calculate_cnt(numeric=numeric)