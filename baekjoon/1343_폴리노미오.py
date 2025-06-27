def get_input():
    board = input()

    return board


def greedy_search(board: str):
    a_value = 'AAAA'
    b_value = 'BB'

    board = board.replace('XXXX', a_value).replace('XX', b_value)

    if 'X' in board:
        print('-1')
    else:
        print(board)


if __name__ == '__main__':
    board = get_input()
    greedy_search(board=board)
