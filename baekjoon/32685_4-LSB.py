import sys


def get_input():
    decimal_nums = []

    for _ in range(3):
        decimal_nums.append(int(sys.stdin.readline()))

    return decimal_nums

def get_password(decimal_nums):
    password = ''

    for num in decimal_nums:
        password += bin(num)[2:].zfill(4)[-4:]

    print(str(int(password, 2)).zfill(4))

if __name__ == '__main__':
    decimal_nums = get_input()
    get_password(decimal_nums=decimal_nums)
