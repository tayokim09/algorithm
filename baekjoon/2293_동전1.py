def get_input():
    coin_cnt, total_value = map(int, input().split(' '))

    # coin_infos = sorted([int(input()) for _ in range(coin_cnt)])
    coin_infos = [int(input()) for _ in range(coin_cnt)]

    return total_value, coin_infos


def get_cases(total_value, coin_infos):
    dp = [0] * (total_value + 1)
    dp[0] = 1

    for coin in coin_infos:
        for i in range(coin, total_value + 1):
            if coin <= i:
                dp[i] = dp[i] + dp[i - coin]

    print(dp[total_value])

if __name__ == '__main__':
    total_value, coin_infos = get_input()
    get_cases(total_value=total_value, coin_infos=coin_infos)