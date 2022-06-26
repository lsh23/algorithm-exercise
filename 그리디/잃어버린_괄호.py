class Solution:
    def solve(self, expr:str ) -> int:
        arr = [ sum([int(x) for x in y.split("+")]) for y in expr.split("-") ]
        return arr[0] - sum(arr[1:])

if __name__ == '__main__':

    expr: str = input()
    s :Solution = Solution()
    answer :int = s.solve(expr)
    print(answer)