import sys

def get_cnt():

    people_cnt, restaurant_cnt = map(int, sys.stdin.readline().split())
    restaurant_rates = []
    max_rate_by_people = {}

    for people in range(people_cnt):
        restaurant_rate = list(map(int, sys.stdin.readline().split()))
        restaurant_rates.append(restaurant_rate)
        max_rate_by_people[people] = max(restaurant_rate)

    change_cnt = []
    for restaurant in range(restaurant_cnt):
        cnt = 0
        for people in range(people_cnt):
            restaurant_rate = restaurant_rates[people][restaurant]
            max_rate = max_rate_by_people[people]

            if restaurant_rate < max_rate:
               cnt += 1

        change_cnt.append(cnt)

    print(*change_cnt)

if __name__ == '__main__':
    get_cnt()
