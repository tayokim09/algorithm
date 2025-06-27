import sys

def search(titles, power):
    lo = 0
    hi = len(titles) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if int(titles[mid][1]) >= power:
            hi = mid
        else:
            lo = mid + 1

    return titles[hi][0]

def get_input():
    title_cnt, character_cnt = map(int, input().split())
    titles = [sys.stdin.readline().split() for _ in range(title_cnt)]
    characters = [int(sys.stdin.readline().strip()) for _ in range(character_cnt)]

    return titles, characters


if __name__ == '__main__':
    titles, characters = get_input()

    for character_power in characters:
        print(search(titles=titles, power=character_power))