def search(n_list, m):
    lo = 0
    hi = len(n_list)

    while lo < hi:
        mid = (lo + hi) // 2

        if n_list[mid] == m:
            return 1

        elif n_list[mid] > m:
            hi = mid
        else:
            lo = mid + 1

    return 0

def get_input():
    n = map(int, input())
    n_list = sorted(set(map(int, input().split())))
    m = map(int, input())
    m_list = list(map(int, input().split()))

    return n_list, m_list


if __name__ == '__main__':
    n_list, m_list = get_input()

    for m in m_list:
        print(search(n_list=n_list, m=m))