class Solution:
    @staticmethod
    def solve(a: str, w: str, s: str):
        shifts: list[int] = []

        a_idx: dict[str, int] = {}
        for i in range(len(a)):
            a_idx[a[i]] = i

        for i in range(len(a)):
            tmp_w = "".join([a[(a_idx[x] + i) % len(a)] for x in w])
            p: list[int] = [0] * len(tmp_w)
            k: int = 0
            for j in range(1, len(tmp_w)):
                while k > 0 and tmp_w[j] != tmp_w[k]:
                    k = p[k - 1]
                if tmp_w[j] == tmp_w[k]:
                    p[j] = k + 1
                    k += 1
            k = 0
            cnt: int = 0
            for j in range(len(s)):
                while k > 0 and s[j] != tmp_w[k]:
                    k = p[k - 1]
                if s[j] == tmp_w[k]:
                    k += 1
                if k == len(tmp_w):
                    k = p[k - 1]
                    cnt += 1

            if cnt == 1:
                shifts.append(str(i))

        if len(shifts) == 0:
            print("no solution")
        elif len(shifts) == 1:
            print(f"unique: {shifts[0]}")
        else:
            print(f"ambiguous: {' '.join(shifts)}")


if __name__ == "__main__":
    N: int
    N = int(input())
    for _ in range(N):
        A: str = input()
        W: str = input()
        S: str = input()
        Solution.solve(A, W, S)
