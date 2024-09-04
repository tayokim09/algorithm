def search(data, dotori_qty):
    lo = 0
    hi = len(data) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if data[mid][0] >= dotori_qty:
            hi = mid
        else:
            lo = mid + 1

    return lo

def get_input():
    hole_cnt = int(input())
    hole_qty_list = [(int(qty) + idx, idx) for idx, qty in enumerate(input().split())]
    hole_qty = [hole_qty_list[0]]

    dotori_cnt = int(input())
    dotori_qty = list(map(int, input().split()))

    for qty in hole_qty_list[1:]:
        if hole_qty[-1][0] < qty[0]:
            hole_qty.append(qty)

    return hole_cnt, hole_qty, dotori_cnt, dotori_qty


if __name__ == '__main__':
    result = []

    hole_cnt, hole_qty, dotori_cnt, dotori_qty = get_input()

    for qty in dotori_qty:
        result.append(str(hole_qty[search(hole_qty, qty)][1] + 1))

    print(' '.join(result))