class Solution:
    @staticmethod
    def solve(start: int, end: int):
        arr = [0]
        for i in range(1, 47):
            arr += [i]*i
        # print(arr)
        return sum(arr[start:end+1])


if __name__ == "__main__":
    start: int
    end: int
    start, end = map(int, input().split())
    print(Solution.solve(start, end))
