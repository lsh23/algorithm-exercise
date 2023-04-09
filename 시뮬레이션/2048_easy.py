def move(board: list[list[int]], direction: str):
    # 0 >
    n: int = len(board)
    if direction == "0":
        # board[i][j] i행의 원소를 역순으로 리스트에 넣고
        # 리스트의 앞 2개가 똑같으면 하나로 합치고 아님 그대로 넣고
        # 리스트 그대로 board[j][i] i행에 역순으로 옮기면 됨
        for i in range(n):
            tmp_list: list[int] = []
            merge_idx = -1
            for j in range(n - 1, -1, -1):
                if board[i][j] != 0:
                    if merge_idx + 1 < len(tmp_list) and tmp_list[-1] == board[i][j]:
                        tmp_list[-1] = tmp_list[-1] * 2
                        merge_idx = len(tmp_list) - 1
                    else:
                        tmp_list.append(board[i][j])
                    board[i][j] = 0
            for j in range(len(tmp_list)):
                board[i][n - 1 - j] = tmp_list[j]
    # 1 ^
    if direction == "1":
        # board[j][i] i열의 원소를 리스트에 넣고
        # 리스트의 앞 2개가 똑같으면 하나로 합치고 아님 그대로 넣고
        # 리스트 그대로 board[j][i] i열에 옮기면 됨
        for i in range(n):
            tmp_list: list[int] = []
            merge_idx = -1
            for j in range(n):
                if board[j][i] != 0:
                    if merge_idx + 1 < len(tmp_list) and tmp_list[-1] == board[j][i]:
                        tmp_list[-1] = tmp_list[-1] * 2
                        merge_idx = len(tmp_list) - 1
                    else:
                        tmp_list.append(board[j][i])
                    board[j][i] = 0
            for j in range(len(tmp_list)):
                board[j][i] = tmp_list[j]

    # 2 <
    if direction == "2":
        # board[i][j] i행의 원소를 리스트에 넣고
        # 리스트의 앞 2개가 똑같으면 하나로 합치고 아님 그대로 넣고
        # 리스트 그대로 board[j][i] i행에 옮기면 됨
        for i in range(n):
            tmp_list: list[int] = []
            merge_idx = -1
            for j in range(n):
                if board[i][j] != 0:
                    if merge_idx + 1 < len(tmp_list) and tmp_list[-1] == board[i][j]:
                        tmp_list[-1] = tmp_list[-1] * 2
                        merge_idx = len(tmp_list) - 1
                    else:
                        tmp_list.append(board[i][j])
                    board[i][j] = 0
            for j in range(len(tmp_list)):
                board[i][j] = tmp_list[j]
    # 3 v
    if direction == "3":
        # board[j][i] i열의 원소를 역순으로 리스트에 넣고
        # 리스트의 앞 2개가 똑같으면 하나로 합치고 아님 그대로 넣고
        # 리스트 그대로 board[j][i] i열에 역순으로 옮기면 됨
        for i in range(n):
            tmp_list: list[int] = []
            merge_idx = -1
            for j in range(n - 1, -1, -1):
                if board[j][i] != 0:
                    if merge_idx + 1 < len(tmp_list) and tmp_list[-1] == board[j][i]:
                        tmp_list[-1] = tmp_list[-1] * 2
                        merge_idx = len(tmp_list) - 1
                    else:
                        tmp_list.append(board[j][i])
                    board[j][i] = 0
            for j in range(len(tmp_list)):
                board[n - 1 - j][i] = tmp_list[j]


def get_max_block(board: list[list[int]]) -> int:
    n: int = len(board)
    max_block: int = 0
    for i in range(n):
        for j in range(n):
            max_block = max(max_block, board[i][j])
    return max_block


class Solution:
    @staticmethod
    def solve(n: int, board: list[list[int]]) -> int:
        ans: int = 0
        # 이동 방향 정하기
        # 0 , 1, 2, 3
        for i in range(1024):
            direction = ""
            while i:
                direction += str(i % 4)
                i //= 4
            direction = direction[::-1]
            direction = direction.zfill(5)
            tmp_board = [[x for x in y] for y in board]

            # print(direction)
            # 이동에 따라 board 반영
            for d in direction:
                move(tmp_board, d)
                ans = max(ans, get_max_block(tmp_board))
                # print("d", d)
                # for t in tmp_board:
                #     print(t)

        return ans


if __name__ == "__main__":
    N: int
    board: list[list[int]]

    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]

    print(Solution.solve(N, board))
