import sys
from typing import Tuple, List
import heapq
class Solution:
    def solve(self, N:int, lectures:Tuple[int,int] ) -> int:

        lectures.sort()
        lecture_rooms: List[int] = []

        for lecture in lectures:
            lecture_start = lecture[0]
            lecture_end = lecture[1]

            if lecture_rooms:
                lecture_room_end = lecture_rooms[0]

                if lecture_room_end <= lecture_start:
                    heapq.heappop(lecture_rooms)
                    heapq.heappush(lecture_rooms,lecture_end)
                else:
                    heapq.heappush(lecture_rooms, lecture_end)
            else:
                heapq.heappush(lecture_rooms,lecture_end)

        # print(lecture_rooms)

        return len(lecture_rooms)



if __name__ == '__main__':
    input = sys.stdin.readline
    N:int = int(input())
    lectures = [ tuple(map(int,input().split())) for _ in range(N) ]
    s :Solution = Solution()
    answer :int = s.solve(N, lectures)
    print(answer)