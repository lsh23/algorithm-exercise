import sys
from heapq import heappush, heappop
if __name__ == '__main__':
    input = sys.stdin.readline
    N: int = int(input())
    heap = []

    for _ in range(N):
        command: int = int(input())
        if command == 0:
            if heap:
                print(heappop(heap)[1])
            else:
                print(0)
        else:
            heappush(heap, (abs(command), command))

