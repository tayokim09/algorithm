import sys


connected_piece = {
        1: [4, 5],
        3: [4, 5],
        4: [2, 3],
        5: [8],
        6: [2, 3],
        7: [8],
        8: [6, 7]
    }


def get_input():

    test_cases = []

    while True:
        test_case = sys.stdin.readline().strip()
        if test_case == '0':
            break

        test_cases.append(test_case)

    return test_cases


def get_result(test_cases):

    for case_num, test_case in enumerate(test_cases):
        is_valid = get_is_valud(test_case)

        print(f"{case_num + 1}. {'VALID' if is_valid else 'NOT'}")


def get_is_valud(test_case):

    if test_case[0] != '1' or test_case[-1] != '2':
        return False

    for i in range(len(test_case) - 1):
        current_piece = int(test_case[i])
        next_piece = int(test_case[i + 1])

        if current_piece == 2:
            return False

        if next_piece not in connected_piece.get(current_piece, []):
            return False

    return True


if __name__ == '__main__':
    test_cases = get_input()
    get_result(test_cases=test_cases)
