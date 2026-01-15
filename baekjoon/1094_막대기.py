def get_input():
    stick_length = int(input())

    return stick_length

def get_count(stick_length):
    cal_cnt = bin(stick_length).count('1')
    print(cal_cnt)


if __name__ == '__main__':
    stick_length = get_input()
    get_count(stick_length=stick_length)
