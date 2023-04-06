class Solution:
    @staticmethod
    def solve2(n: int, w: int, L: int, truck_weight: list[int]) -> int:

        time: int = 0
        complete_truck: int = 0

        truck_on_bridge: list[tuple[int, int]] = []
        weigh_on_bridge: int = 0
        next_truck_idx: int = 0

        while complete_truck != n:
            time += 1

            # 다리위 트럭 이동
            for i in range(len(truck_on_bridge)):
                t = truck_on_bridge[i]
                t_weight = t[0]
                t_time = t[1]
                if t_time >= w:
                    continue
                t_time += 1
                if t_time >= w:
                    # 트럭 삭제
                    complete_truck += 1
                    weigh_on_bridge -= t_weight
                truck_on_bridge[i] = (t_weight, t_time)

            # 현재 다리에 수용 가능한 무게 구하기
            # 다리를 건너려는 트럭이 올라갈 수 있는지
            if next_truck_idx >= n:
                continue
            if L - weigh_on_bridge >= truck_weight[next_truck_idx]:
                truck_on_bridge.append((truck_weight[next_truck_idx], 0))
                weigh_on_bridge += truck_weight[next_truck_idx]
                next_truck_idx += 1

        return time

    @staticmethod
    def solve(n: int, w: int, L: int, truck_weight: list[int]) -> int:
        from collections import deque

        time: int = 0
        weigh_on_bridge: int = 0
        complete_truck: int = 0
        next_truck_idx: int = 0

        q: deque = deque()

        while complete_truck != n:
            time += 1

            # 다리위 트럭 이동
            for i in range(len(q)):
                q[i] = (q[i][0], q[i][1] + 1)

            if q and q[0][1] == w:
                out_truck = q.popleft()
                weigh_on_bridge -= out_truck[0]
                complete_truck += 1

            # 현재 다리에 수용 가능한 무게 구하기
            # 다리를 건너려는 트럭이 올라갈 수 있는지
            if next_truck_idx >= n:
                continue
            if L - weigh_on_bridge >= truck_weight[next_truck_idx]:
                q.append((truck_weight[next_truck_idx], 0))
                weigh_on_bridge += truck_weight[next_truck_idx]
                next_truck_idx += 1

        return time


if __name__ == "__main__":
    n: int
    w: int
    L: int
    truck_weight: list[int]
    n, w, L = map(int, input().split())
    truck_weight = [int(x) for x in input().split()]
    print(Solution.solve(n, w, L, truck_weight))
