import sys


def get_input():
    alphabets = (1 << 26) - 1
    words = []

    word_cnt, query_cnt = map(int, sys.stdin.readline().split())

    for _ in range(word_cnt):
        word = sys.stdin.readline().strip()
        bit_word = 0

        for char in word:
            bit_word |= (1 << (ord(char) - 97))

        words.append(bit_word)

    for _ in range(query_cnt):
        is_remember, char = sys.stdin.readline().split()
        char = 1 << (ord(char) - 97)

        if is_remember == '1':
            alphabets &= ~char
        else:
            alphabets |= char

        cnt = 0

        for word in words:
            if (alphabets & word) == word:
                cnt += 1

        print(cnt)


if __name__ == '__main__':
    get_input()
