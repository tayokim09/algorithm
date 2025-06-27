def _is_in(n_list, m_list):
    for m in m_list:
        if m in n_list:
            print(1)
        else:
            print(0)


def get_input():
    n = map(int, input())
    n_list = set(map(int, input().split()))
    m = map(int, input())
    m_list = list(map(int, input().split()))

    return n_list, m_list


if __name__ == '__main__':
    n_list, m_list = get_input()
    _is_in(n_list=n_list, m_list=m_list)