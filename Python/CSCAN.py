import random
from typing import List

SIZE = 16
DISK_SIZE = 1 << 8


def CSCAN(arr: List[int], head: int, end=DISK_SIZE) -> float:
    requests = {}
    sequence = []
    print('Head is at:', head)
    print('Original sequence:   ', *arr)
    for i in arr:
        requests[i] = None
    pos = head
    start = time = 0
    end = end
    n = len(arr)
    for i in range(pos, end + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            sequence.append(i)
            requests.pop(i)
    time += abs(pos - end)
    pos = end
    for i in range(start, head + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            sequence.append(i)
            requests.pop(i)

    print("Seek sequence is:    ", *sequence)
    print("Total number of seek operations:", time)

    return time / n


def main():
    print()
    print('-*' * 10, '     CSCAN    ', '*-' * 10)
    print()
    arr = random.sample(range(1, DISK_SIZE + 1), SIZE)
    head = random.randint(1, 1 << 4)
    print('Avg seek time: {:.5f} units'.format(CSCAN(arr, head)))
    print()
    return


if __name__ == '__main__':
    main()
