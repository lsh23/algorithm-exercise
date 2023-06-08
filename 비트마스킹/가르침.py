def is_readable(word: int, selected_alphabets: int) -> bool:
    return (word & selected_alphabets) == word


class Solution:
    @staticmethod
    def solve(n: int, k: int, words: list[int]) -> int:
        answer: int = 0

        if k < 5:
            return 0

        if k == 26:
            return n

        def select(l: int, cur: int, selected: int):
            nonlocal answer
            if l == k:
                cnt: int = 0
                for word in words:
                    if is_readable(word, selected):
                        cnt += 1
                answer = max(cnt, answer)
            else:
                for i in range(cur, 26):
                    if selected & (1 << i) == 0:
                        selected |= (1 << i)
                        select(l + 1, i + 1, selected)
                        selected ^= (1 << i)

        selected: int = 0
        selected |= (1 << (ord('a') - ord('a')))
        selected |= (1 << (ord('n') - ord('a')))
        selected |= (1 << (ord('t') - ord('a')))
        selected |= (1 << (ord('c') - ord('a')))
        selected |= (1 << (ord('i') - ord('a')))
        select(5, 0, selected)

        return answer


if __name__ == "__main__":
    N: int
    K: int
    N, K = map(int, input().split())
    words: list[int] = []
    for _ in range(N):
        word_str: str = input()
        word: int = 0
        for c in word_str:
            word |= (1 << ord(c) - ord('a'))
        words.append(word)
    print(Solution.solve(N, K, words))
