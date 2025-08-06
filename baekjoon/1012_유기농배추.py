from collections import deque


def get_input():
    test_cnt = int(input())

    graph_info = []
    graphs = []

    for _ in range(test_cnt):
        width, height, cabbage = map(int, input().split(' '))

        graph_info.append((width, height))
        tmp_graph = [[0] * (width) for _ in range(height)]

        for _ in range(cabbage):
            x, y = map(int, input().split())
            tmp_graph[y][x] = 1

        graphs.append(tmp_graph)

    return test_cnt, graph_info, graphs


def bfs(width, height, x, y, graph):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for x_interval, y_interval in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_move = x + x_interval
            y_move = y + y_interval

            if 0 <= x_move < width and 0 <= y_move < height and graph[y_move][x_move]:
                graph[y_move][x_move] = 0
                queue.append((x_move, y_move))


def get_earthworm_cnt(test_cnt, graph_info, graphs):

    for idx in range(test_cnt):
        earthworm_cnt = 0
        width, height = graph_info[idx]
        graph = graphs[idx]

        for x in range(width):
            for y in range(height):
                if graph[y][x] == 1:
                    bfs(width=width, height=height, x=x, y=y, graph=graph)
                    earthworm_cnt += 1

        print(earthworm_cnt)

if __name__ == '__main__':
    test_cnt, graph_info, graphs = get_input()
    get_earthworm_cnt(test_cnt=test_cnt, graph_info=graph_info, graphs=graphs)



