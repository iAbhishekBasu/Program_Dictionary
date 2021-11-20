import random
import heapq
from typing import List

SIZE = 16
DISK_SIZE = 1 << 8


def SSTF(arr: List[int], head: int) -> float:
    print('Head is at:', head)
    print('Original sequence:   ', *arr)
    requests = {}
    sequence = []
    heap = []
    for i in arr:
        requests[i] = None
    time = 0
    position = head
    n = len(requests)
    for _ in range(n):
        for r in requests:
            heapq.heappush(heap, (abs(position - r), r))
        x = heapq.heappop(heap)[1]
        time += abs(position - x)
        position = x
        sequence.append(x)
        requests.pop(x)
        heap = []
    print("Seek sequence is:    ", *sequence)
    print("Total number of seek operations:", time)

    return time / n


def main():
    print()
    print('-*' * 10, '     SSTF    ', '*-' * 10)
    print()
    arr = random.sample(range(1, DISK_SIZE + 1), SIZE)
    head = random.randint(1, 1 << 8)
    print('Avg seek time: {:.5f} units'.format(SSTF(arr, head)))
    print()
    return


if __name__ == '__main__':
    main()
