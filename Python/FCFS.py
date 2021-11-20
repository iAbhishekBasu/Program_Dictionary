import random
from typing import List

SIZE = 16
DISK_SIZE = 1 << 8


def FCFS(arr: List[int], head: int) -> float:
    print('Head is at:', head)
    print('Original sequence:   ', *arr)
    time = 0
    for request in arr:
        distance = abs(request - head)
        time += distance
        head = request

    print("Seek sequence is:    ", *arr)
    print("Total number of seek operations:", time)

    return time / len(arr)


def main():
    print()
    print('-*' * 10, '     FCFS    ', '*-' * 10)
    print()
    arr = random.sample(range(1, DISK_SIZE + 1), SIZE)
    head = random.randint(1, 1 << 4)
    print('Avg seek time: {:.5f} units'.format(FCFS(arr, head)))
    print()
    return


if __name__ == '__main__':
    main()
