import sys


def get_input():
    a, b = map(int, sys.stdin.readline().split())

    return a, b


def get_c_score(a_score, b_score):
    print(a_score ^ b_score)

if __name__ == '__main__':
    a_score, b_score = get_input()
    get_c_score(a_score=a_score, b_score=b_score)
