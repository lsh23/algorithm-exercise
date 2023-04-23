class Solution:
    @staticmethod
    def solve(n: int, k: int, a: int) -> int:

        belt: list[int] = [[durability, 0] for durability in a]
        step: int = 0
        while True:
            step += 1

            # 1. 벨트 회전
            # 벭트의 내구도뿐만 아니라 벨트위의 로봇도 같이 움직여아함
            after_belt = [x for x in belt]
            for i in range(2 * n):
                after_belt[i] = belt[(i - 1) % (2 * n)]
                durability, is_robot = after_belt[i]
                if i == n - 1 and is_robot == 1:
                    after_belt[i][1] = 0

            # 2. 가장 먼저 올라간 로봇 부터, 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동한다.
            for i in range(n - 2, 0, -1):
                durability, is_robot = after_belt[i]
                if is_robot == 0:
                    continue
                next_durability, next_is_robot = after_belt[i + 1]
                if next_durability > 0 and next_is_robot == 0:
                    after_belt[i][1] = 0
                    after_belt[i + 1][1] = 1
                    after_belt[i + 1][0] -= 1
                    if i + 1 == n - 1:
                        after_belt[i + 1][1] = 0

            # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
            if after_belt[0][0] > 0:
                after_belt[0][0] -= 1
                after_belt[0][1] = 1

            # 4. 내구도가 0인 칸의 개수가 K개 이상이면 종료, 아니면 계속
            cnt: int = 0
            for i in range(2 * n):
                if after_belt[i][0] == 0:
                    cnt += 1
                if cnt == k:
                    break
            if cnt == k:
                break

            belt = after_belt

        return step


if __name__ == "__main__":
    N: int
    K: int
    A: list[int]
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    print(Solution.solve(N, K, A))
