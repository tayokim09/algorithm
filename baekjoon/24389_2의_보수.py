def get_input():
    number = int(input())

    return number

def get_diff_of_bit(number):
    bin_number = bin(number)[2:].zfill(32)
    reverse_bin = ''.join([str(abs(int(num) - 1)) for num in bin_number])
    reverse_bin = bin(int(reverse_bin, 2) + 1)[2:].zfill(32)

    diff = 0

    for num, reverse_num in zip(bin_number, reverse_bin):
        if num != reverse_num:
            diff += 1

    print(diff)

if __name__ == '__main__':
    number = get_input()
    get_diff_of_bit(number=number)
