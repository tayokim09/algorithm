def get_input():
    n_kg = int(input())

    return n_kg


def min_atm_time(n_kg):
    if n_kg % 5 == 0:
        print(n_kg // 5)
        return

    for i in range(n_kg // 3):
        remain = n_kg - (3 * i)

        if remain % 5 == 0:
            print((remain // 5) + i)
            return

    if n_kg % 3 == 0:
        print(n_kg // 3)
        return

    print(-1)


if __name__ == '__main__':
    n_kg = get_input()
    min_atm_time(n_kg=n_kg)
