import sys

DAY_TO_MIN = 1440

def get_bus_time():

    arrival_hour, arrival_min = map(int, sys.stdin.readline().split())
    arrival_time = arrival_hour * 60 + arrival_min

    bus_line_cnt = int(sys.stdin.readline())
    bus_times = []

    for _ in range(bus_line_cnt):

        first_hour, first_min, interval = map(int, sys.stdin.readline().split())
        bus_time = first_hour * 60 + first_min
        bus_times.append(bus_time + DAY_TO_MIN)

        while bus_time < DAY_TO_MIN:
            if bus_time >= arrival_time:
                bus_times.append(bus_time)

            bus_time += interval

    bus_time = min(bus_times)
    bus_time = bus_time % DAY_TO_MIN
    bus_time_hour = bus_time // 60
    bus_time_min = bus_time % 60

    print(f"{bus_time_hour:02d}:{bus_time_min:02d}")

if __name__ == '__main__':
    get_bus_time()
