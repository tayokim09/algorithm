import sys

vowel = ['A', 'E', 'I', 'O', 'U']

def get_contest_name():

    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    if len(s) < m:
        print('NO')
        return

    idx_s = -1
    idx_a1 = -1
    idx_a2 = -1

    curr = n - 1
    while curr >= 0:
        if s[curr] not in vowel:
            idx_s = curr
            curr -= 1
            break
        curr -= 1

    while curr >= 0:
        if s[curr] == 'A':
            idx_a1 = curr
            curr -= 1
            break
        curr -= 1

    while curr >= 0:
        if s[curr] == 'A':
            idx_a2 = curr
            curr -= 1
            break
        curr -= 1

    if idx_s == -1 or idx_a1 == -1 or idx_a2 == -1 or idx_a2 < m - 3:
        print('NO')
        return

    print('YES')
    print(s[idx_a2-(m-3) : idx_a2] + "AA" + s[idx_s])


if __name__ == '__main__':
    get_contest_name()
