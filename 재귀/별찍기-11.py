class Solution:
    def solve(self,N: int) -> None:
        def star(N: int):
            if N == 3:
                return ['  *  ', ' * * ', '*****']
            arr: list[str] = star(N//2)
            stars: list[str] = []

            for i in arr:
                stars.append(' '*(N//2)+i+' '*(N//2))

            for i in arr:
                stars.append(i+' '+i)
            return stars

        return '\n'.join(star(N))


if __name__ == '__main__':
    N: int = int(input())
    s :Solution = Solution()
    print(s.solve(N))