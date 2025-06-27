def get_input():
    numeric = int(input())
    test_cases = [int(input()) for _ in range(numeric)]

    return test_cases


def get_calculate_cnt(test_cases):
    dp = {1:1, 2:2, 3:4}
    max_neumeric = max(test_cases)

    for i in range(4, max_neumeric + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for test_case in test_cases:
        print(dp[test_case])


if __name__ == '__main__':
    test_cases = get_input()
    get_calculate_cnt(test_cases=test_cases)