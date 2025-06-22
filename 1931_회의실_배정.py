def get_input():
    meet_cnt = int(input())
    meet_times = []

    for i in range(meet_cnt):
        meet_time = tuple(map(int, input().split(' ')))
        meet_times.append(meet_time)

    meet_times = sorted(meet_times, key=lambda x: (x[1], x[0]))

    return meet_times

def get_max_meet_cnt(meet_times):
    meet_cnt = 1
    now_meet = meet_times[0]

    for meet_time in meet_times[1:]:
        if now_meet[1] <= meet_time[0]:
            now_meet = meet_time
            meet_cnt += 1

    print(meet_cnt)

if __name__ == '__main__':
    meet_times = get_input()
    get_max_meet_cnt(meet_times=meet_times)