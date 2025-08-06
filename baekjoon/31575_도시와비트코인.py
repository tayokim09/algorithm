from collections import deque


def get_input():
    width, height = map(int, input().split(' '))

    graph = [list(map(int, input().split(' '))) for _ in range(height)]

    return width, height, graph


def bfs(width, height, graph):
    queue = deque([(0, 0)])

    if width == 1 and height == 1:
        print('Yes')
        return

    while queue:
        x, y = queue.popleft()

        for x_interval, y_interval in [(0, 1), (1, 0)]:
            x_move = x + x_interval
            y_move = y + y_interval

            if x_move == width - 1 and y_move == height - 1:
                print('Yes')
                return

            if x_move < width and y_move < height and graph[y_move][x_move]:
                graph[y_move][x_move] = 0
                queue.append((x_move, y_move))

    print('No')


if __name__=='__main__':
    width, height, graph = get_input()
    bfs(width=width, height=height, graph=graph)
