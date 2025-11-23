import sys
from collections import deque


def get_input():
    people_cnt = int(sys.stdin.readline().strip())

    graph = {}

    while True:

        member1, member2 = map(int, sys.stdin.readline().strip().split())

        if (member1, member2) == (-1, -1):
            break

        if member1 not in graph:
            graph[member1] = []

        if member2 not in graph:
            graph[member2] = []

        graph[member1].append(member2)
        graph[member2].append(member1)

    return people_cnt, graph


def get_candidate(people_cnt, graph):
    scores = []

    for member in range(1, people_cnt + 1):
        scores.append(bfs(people_cnt=people_cnt, start=member, graph=graph))

    min_score = min(scores)

    candidates = [index + 1for index in range(len(scores)) if scores[index] == min_score]

    print(min_score, len(candidates))
    print(*candidates)

def bfs(people_cnt, start, graph):
    score = [sys.maxsize] * (people_cnt + 1)
    queue = deque()
    queue.append(start)
    score[start] = 0

    while queue:
        member = queue.popleft()

        for friend in graph[member]:

            if score[friend] == sys.maxsize:
                score[friend] = score[member] + 1
                queue.append(friend)

    return max(score[1:])


if __name__ == '__main__':
    people_cnt, graph = get_input()
    get_candidate(people_cnt=people_cnt, graph=graph)
