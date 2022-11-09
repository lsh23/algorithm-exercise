class Solution:
    def solve(self,N: int) -> int:

        def star(N:int):
            if N == 3:
                return ['***', '* *', '***']

            arr: List[str] = star(N//3)
            stars: List[str] = []

            for i in arr:
                stars.append(i*3)

            for i in arr:
                stars.append(i+' '*(N//3)+i)

            for i in arr:
                stars.append(i*3)

            return stars

        return '\n'.join(star(N))


if __name__ == '__main__':
    N: int = int(input())
    s :Solution = Solution()
    print(s.solve(N))