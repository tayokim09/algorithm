def get_input():
    leak_cnt, tape_lenth = map(int, input().split(' '))
    leak_points = sorted(map(int, input().split(' ')))

    return leak_cnt, tape_lenth, leak_points


def get_tape_cnt(leak_cnt, tape_lenth, leak_points):
    tape_point_x = None
    tape_cnt = 0

    for leak_point in leak_points:
        if tape_point_x and tape_point_x + tape_lenth >= leak_point:
            continue

        tape_point_x = leak_point - 0.5
        tape_cnt += 1

    print(tape_cnt)


if __name__ == '__main__':
    leak_cnt, tape_lenth, leak_points = get_input()
    get_tape_cnt(leak_cnt=leak_cnt, tape_lenth=tape_lenth, leak_points=leak_points)
