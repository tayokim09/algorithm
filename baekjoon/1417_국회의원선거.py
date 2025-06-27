def get_input():
    candidate = int(input())
    vote_by_candidate = {}

    for idx in range(candidate):
        vote_by_candidate[idx] = (int(input()))

    return vote_by_candidate


def greedy_search(vote_by_candidate):
    n = 0

    while True:
        max_candidate = max(vote_by_candidate, key=vote_by_candidate.get)

        if max_candidate == 0:
            if list(vote_by_candidate.values()).count(vote_by_candidate[max_candidate]) != 1:
                n += 1
            break

        vote_by_candidate[max_candidate] -= 1
        vote_by_candidate[0] += 1
        n += 1

    print(n)


if __name__ == '__main__':
    vote_by_candidate = get_input()
    greedy_search(vote_by_candidate=vote_by_candidate)
