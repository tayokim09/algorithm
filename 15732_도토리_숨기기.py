def is_packaging_dotori(box_idx, dotori_qty, rules):
    packaging_qty = 0

    for box_start_idx, box_end_idx, step in rules:
        if box_idx < box_start_idx: continue
        box_end_idx = min(box_idx, box_end_idx)
        packaging_qty += ((box_end_idx - box_start_idx) // step) + 1

    return packaging_qty >= dotori_qty


def search(max_box_cnt, dotori_qty, rules):
    lo = 0
    hi = max_box_cnt

    while lo < hi:
        mid = (lo + hi) // 2
        if is_packaging_dotori(box_idx=mid, dotori_qty=dotori_qty, rules=rules):
            hi = mid
        else:
            lo = mid + 1

    return lo


def get_input():
    max_box_cnt, rule_cnt, dotori_qty = list(map(int, input().split()))
    rules = [list(map(int, input().split())) for _ in range(rule_cnt)]

    return max_box_cnt, rules, dotori_qty


if __name__ == '__main__':
    max_box_cnt, rules, dotori_qty = get_input()
    print(search(max_box_cnt=max_box_cnt, dotori_qty=dotori_qty, rules=rules))