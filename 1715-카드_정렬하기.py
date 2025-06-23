from queue import PriorityQueue


def get_input():
    card_cnt = int(input())

    queue = PriorityQueue(maxsize=card_cnt)

    for _ in range(card_cnt):
        queue.put(int(input()))

    return queue


def get_min_comparison(queue):
    comparison_cnt = 0

    while queue.qsize() != 1:
        list_cnt1 = queue.get()
        list_cnt2 = queue.get()

        comparison_cnt += list_cnt1 + list_cnt2

        queue.put(list_cnt1 + list_cnt2)

    print(comparison_cnt)



if __name__=='__main__':
    queue = get_input()
    get_min_comparison(queue=queue)
