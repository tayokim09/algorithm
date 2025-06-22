def get_input():
    country_cnt = int(input())
    road = list(map(int, input().split(' ')))
    gas_fees = list(map(int, input().split(' ')))

    return country_cnt, road, gas_fees


def get_min_gas_fee(country_cnt, road, gas_fees):
    total_gas_fee = road[0] * gas_fees[0]
    gas_fee = gas_fees[0]

    for country_idx in range(1, country_cnt - 1):
        gas_fee = min(gas_fee, gas_fees[country_idx])
        total_gas_fee += road[country_idx] * gas_fee

    print(total_gas_fee)


if __name__ == '__main__':
    country_cnt, road, gas_fees = get_input()
    get_min_gas_fee(country_cnt=country_cnt, road=road, gas_fees=gas_fees)
