class Solution:
    @staticmethod
    def solve(input_string: str) -> int:
        answer: int = 1000
        cnt_a: int = input_string.count('a')
        tmp_string: str = input_string + input_string
        for i in range(len(tmp_string) - (cnt_a - 1)):
            left: int = i
            right: int = i + cnt_a - 1
            change_cnt = tmp_string[left:right + 1].count('b')
            answer = min(change_cnt, answer)
        return answer


if __name__ == "__main__":
    input_string: str = input()
    print(Solution.solve(input_string))
