def get_input():
    n = int(input())
    bin_num = input()

    return bin_num

def get_count(bin_num):
    print(bin_num.count('1'))

if __name__ == '__main__':
    bin_num = get_input()
    get_count(bin_num=bin_num)
