class Solution:
    def solve(self, N: int, M: int, K: int, tile: list[list[str]], got_strings: list[str]):
        # tile로 길이가 5인 스트링 만듦면서 해시 테이블에 값 기록
        # 이후 got string으로 갯수 조회

        string_count: dict[str, int] = {}

        dx = [0,1,0,-1,1,-1,1,-1]
        dy = [1,0,-1,0,1,-1,-1,1]

        def dfs(L: int, y:int, x:int, string:str):
            if string in string_count:
                string_count[string] += 1
            else:
                string_count[string] = 1
            if L == 6:
                return
            for i in range(8):
                next_y = (y + dy[i]) % N
                next_x = (x + dx[i]) % M
                dfs(L+1, next_y, next_x, string+tile[next_y][next_x])

        for i in range(N):
            for j in range(M):
                dfs(1 ,i, j, tile[i][j])

        # print(string_count)
        for s in got_strings:
            if s in string_count:
                print(string_count[s])
            else:
                print(0)


if __name__ == "__main__":
    N: int
    M: int
    K: int

    N, M, K = map(int,input().split())
    tile: list[list[str]] = []
    got_strings: list[str] = []

    for _ in range(N):
        tile.append([x for x in input()])
    assert len(tile) == N
    assert len(tile[0]) == M

    for _ in range(K):
        got_strings.append(input())
    assert len(got_strings) == K

    s: Solution = Solution()
    s.solve(N, M, K, tile, got_strings)

