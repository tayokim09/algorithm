def get_input():
    people = int(input())
    atm_time = list(map(int, input().split(' ')))

    return people, atm_time


def min_atm_time(people, atm_time):
    n = 0

    for time in sorted(atm_time):
        n += time * people
        people -= 1

    print(n)


if __name__ == '__main__':
    people, atm_time = get_input()
    min_atm_time(people=people, atm_time=atm_time)
