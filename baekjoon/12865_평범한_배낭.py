def get_input():
    prod_cnt, weight = map(int, input().split(' '))

    prod_infos = sorted([tuple(map(int, input().split(' '))) for _ in range(prod_cnt)], key=lambda x: x[0])

    return weight, prod_infos


def get_max_value(weight, prod_infos):
    dp = [[0] * (len(prod_infos) + 1) for _ in range(weight + 1)]

    for i in range(1, weight + 1):
        for j in range(1, len(prod_infos) + 1):
            prod_weight = prod_infos[j - 1][0]
            value = prod_infos[j - 1][1]

            if prod_infos[j - 1][0] <= i:
                dp[i][j] = max(dp[i][j - 1], dp[i - prod_weight][j - 1] + value)
                continue

            dp[i][j] = dp[i][j - 1]

    print(max(dp[weight]))


if __name__ == '__main__':
    weight, prod_infos = get_input()
    get_max_value(weight=weight, prod_infos=prod_infos)