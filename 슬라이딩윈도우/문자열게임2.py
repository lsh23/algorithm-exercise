class Solution:
    @staticmethod
    def solve(w: str, k: int) -> int:
        appearance_idx: list[list[int]] = [[] for _ in range(26)]
        w_len = len(w)

        for i in range(w_len):
            appearance_idx[ord(w[i]) - ord('a')].append(i)

        # print(appearance_idx)

        min_length: int = 10_001
        min_length_str: str = ""
        max_length: int = 0
        max_length_str: str = ""
        for x in range(26):
            idx_list = appearance_idx[x]
            if len(idx_list) < k:
                continue
            for i in range(len(idx_list)):
                j = i + (k - 1)
                if j >= len(idx_list):
                    continue
                tmp = w[idx_list[i]:idx_list[j] + 1]
                if tmp.count(chr(ord('a') + x)) == k:
                    if max_length < len(tmp):
                        max_length = len(tmp)
                        max_length_str = tmp
                    if min_length > len(tmp):
                        min_length = len(tmp)
                        min_length_str = tmp

        # print(min_length)
        # print(min_length_str)
        # print(max_length)
        # print(max_length_str)

        if min_length == 10_001 and max_length == 0:
            print(-1)
        else:
            print(min_length, max_length)


if __name__ == "__main__":
    T: int
    T = int(input())
    for _ in range(T):
        W: str
        K: int
        W = input()
        K = int(input())
        Solution.solve(W, K)
