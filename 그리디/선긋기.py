import sys
from typing import List, Tuple
class Solution:
    def solve(self, lines: List[Tuple[int,int]]) -> int:

        total_len: int = 0
        lines.sort(reverse=True)

        # top의 시작점이 이전 라인 사이에 있으면
            # 새로 그어진 만큼 선분에 길이 더함
        # 없으면
            # 새로 시작하는 만큼 선분 길이 더함

        prev_line_end: int = -1000000000
        while lines:
            new_line = lines.pop()
            new_line_start = new_line[0]
            new_line_end = new_line[1]

            if new_line_start <= prev_line_end:
                if new_line_end > prev_line_end:
                    total_len += (new_line_end - prev_line_end)
                    prev_line_end = new_line_end
            else:
                total_len += (new_line_end - new_line_start)
                prev_line_end = new_line_end

            # print(new_line, total_len, prev_line_end_x_axis)

        return total_len

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    lines = [ tuple(map(int,input().split())) for _ in range(N) ]
    s :Solution = Solution()
    answer :int = s.solve(lines)
    print(answer)