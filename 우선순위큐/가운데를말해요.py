import heapq
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N: int = int(input())
    max_heap: list[int] = []
    min_heap: list[int] = []
    for _ in range(N):
        number: int = int(input())

        if len(max_heap) == len(min_heap):  # 길이 보정 로직 항상 max heap의 원소 개수가 1개 많거나 같도록 함
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)

        if min_heap and min_heap[0] < -max_heap[0]:
            max_top = -heapq.heappop(max_heap)
            min_top = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_top)
            heapq.heappush(min_heap, max_top)

        print(-max_heap[0])
