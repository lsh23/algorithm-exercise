class Solution:
    @staticmethod
    def solve(n: int, numbers: list[int]) -> int:
        answer: int = 0
        number_cnt: dict[int, int] = {}
        for number in numbers:
            if number in number_cnt:
                number_cnt[number] += 1
                continue
            number_cnt[number] = 1
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                find = numbers[i] - numbers[j]
                if find not in number_cnt:
                    continue
                number_cnt[numbers[j]] -= 1
                number_cnt[numbers[i]] -= 1
                if number_cnt[find] >= 1:
                    answer += 1
                    number_cnt[numbers[j]] += 1
                    number_cnt[numbers[i]] += 1
                    break
                number_cnt[numbers[j]] += 1
                number_cnt[numbers[i]] += 1
        return answer

    @staticmethod
    def solve_tow_pointer(n: int, numbers: list[int]) -> int:
        answer: int = 0
        numbers.sort()
        for i in range(n):
            tmp: list[int] = numbers[:i] + numbers[i + 1:]
            left: int = 0
            right: int = n - 2
            while left < right:
                sum = tmp[left] + tmp[right]
                if sum == numbers[i]:
                    answer += 1
                    break
                if sum < numbers[i]:
                    left += 1
                else:
                    right -= 1
        return answer


if __name__ == "__main__":
    N: int
    numbers: list[int]
    N = int(input())
    numbers = [int(x) for x in input().split()]
    print(Solution.solve(N, numbers))
    # print(Solution.solve_tow_pointer(N, numbers))
