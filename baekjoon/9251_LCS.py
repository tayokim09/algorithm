def get_input():
    first_word = input()
    second_word = input()

    return first_word, second_word


def get_lcs_length(first_word, second_word):
    sub_sequence = [[0] * (len(second_word) + 1) for _ in range(len(first_word) + 1)]

    for i in range(1, len(first_word)  + 1):
        for j in range(1, len(second_word) + 1):
            if first_word[i - 1] == second_word[j - 1]:
                sub_sequence[i][j] = sub_sequence[i - 1][j - 1] + 1
            else:
                sub_sequence[i][j] = max(sub_sequence[i][j - 1], sub_sequence[i - 1][j])

    print(max(map(max, sub_sequence)))


if __name__=='__main__':
    first_word, second_word = get_input()
    get_lcs_length(first_word=first_word, second_word=second_word)