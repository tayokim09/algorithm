import sys
import math


def insert_evidence_to_array(array, bs_evidence):
    lo = 0
    hi = len(array) - 1

    for index in range(len(bs_evidence)):
        evidence = bs_evidence[index]
        next_evidence = None if index == len(bs_evidence) - 1 else bs_evidence[index + 1]

        mid = (lo + hi) // 2

        array[mid] = evidence

        if next_evidence is None:
            return array

        elif next_evidence < evidence:
            hi = mid - 1

        elif next_evidence > evidence:
            lo = mid + 1

    return array


def calculate_array_cnt(array, comb_r):
    array_cnt = 1
    no_value_cnt = 0

    for index in range(len(comb_r)):
        r = comb_r[index]

        if index == len(comb_r) - 1:
            start_value = 0 if r - no_value_cnt - 1 < 0 else array[r - no_value_cnt - 1]
            end_value = 100 if r == len(array) - 1 else array[r + 1] - 1

            array_cnt *= math.comb(end_value - start_value, no_value_cnt + 1)
            break

        next_r = comb_r[index + 1]

        if next_r - r == 1:
            no_value_cnt += 1

        elif next_r - r != 1 and comb_r[index] == 0:
            array_cnt *= array[r + 1] - 1

        else:
            start_value = 0 if r - no_value_cnt - 1 < 0 else array[r - no_value_cnt - 1]
            end_value = array[r + 1]
            array_cnt *= math.comb(end_value - start_value - 1, no_value_cnt + 1)
            no_value_cnt = 0

    return array_cnt


def get_input():
    length, bs_evidence_cnt = map(int, input().split())
    bs_evidence = list(map(int, sys.stdin.readline().split()))
    array = [-1 for _ in range(length)]

    return array, bs_evidence


if __name__ == '__main__':
    array, bs_evidence = get_input()

    array = insert_evidence_to_array(array=array, bs_evidence=bs_evidence)
    comb_r = list(filter(lambda x: array[x] == -1, range(len(array))))
    array_cnt = calculate_array_cnt(array=array, comb_r=comb_r)

    print(array_cnt % 1000000007)
