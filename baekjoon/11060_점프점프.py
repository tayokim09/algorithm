from collections import deque
import sys


def get_input():
    n = int(sys.stdin.readline().strip())

    jump_distances = []
    jump_distances.extend(map(int, sys.stdin.readline().strip().split()))

    return n, jump_distances


def bfs(n, jump_distances):
    if n == 1:
        return 0

    visited = [0 for _ in range(len(jump_distances) + 1)]
    queue = deque([0])
    jump_idx = 0

    while queue:
        position = queue.popleft()

        for distance in range(0, jump_distances[jump_idx] + 1):
            if not visited[position + distance]:
                if position + distance >= n:
                    return jump_idx

                queue.append(position + distance)

        jump_idx += 1

    return -1


if __name__ == '__main__':
    n, jump_distances = get_input()

    print(bfs(n=n, jump_distances=jump_distances))