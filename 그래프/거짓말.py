from typing import List
class Solution:
    def solve(self, N:int, k_members:List[int], graph:List[List[int]], party_info:List[List[int]] ) -> int:

        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = 1

        # for i in range(1,N+1):
        #     for j in range(1,N+1):
        #         print(graph[i][j], end=" ")
        #     print()

        answer: int = 0
        for p_members in party_info:
            is_k_member_attend: bool = False
            for member in p_members:
                for k_member in k_members:
                    if member == k_member or graph[k_member][member] == 1:
                        is_k_member_attend = True
                        break
                if is_k_member_attend:
                    break
            if is_k_member_attend is False:
                # print(p_members,"--")
                answer += 1

        return answer

if __name__ == '__main__':
    N: int
    M: int
    N, M = map(int,input().split())
    graph = [ [0]*(N+1) for _ in range(N+1) ]
    tmp = [ int(x) for x in input().split()]
    k_n = tmp[0]
    k_members = tmp[1:]

    party_info: List[List[int]] = []
    for _ in range(M):
        tmp = [ int(x) for x in input().split() ]
        p_members = tmp[1:]
        party_info.append(p_members)
        len_p_members = len(p_members)
        for i in range(len_p_members-1):
            graph[p_members[i]][p_members[i+1]] = 1
            graph[p_members[i+1]][p_members[i]] = 1

    s :Solution = Solution()
    print(s.solve(N,k_members,graph,party_info))






