from collections import deque

def get_input():
    start = int(input().strip(), 2)
    end = int(input().strip(), 2)

    return start, end

def get_count(start, end):
    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        nx, cnt = queue.popleft()
        bin_nx = bin(nx)[2:]

        if nx == end:
            print(cnt)
            return

        for i in range(len(bin_nx) - 1):
            dx = nx ^ (1 << i)
            if dx not in visited:
                visited.add(dx)
                queue.append((dx, cnt + 1))

        dx = nx + 1
        if dx not in visited:
            visited.add(dx)
            queue.append((dx, cnt + 1))

        if nx == 0:
            continue

        dx = nx - 1
        if dx not in visited:
            visited.add(dx)
            queue.append((dx, cnt + 1))


if __name__ == '__main__':
    start, end = get_input()
    get_count(start=start, end=end)
