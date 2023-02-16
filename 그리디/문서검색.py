class Solution:
    def solve(self, docs:str, word:str) -> int:

        cnt: int = 0
        while True:
            i:int = docs.find(word)
            if i == -1:
                break
            docs = docs[i+len(word):]
            cnt+=1

        return cnt


if __name__ == "__main__":
    docs: str = input()
    word: str = input()
    s = Solution()
    print(s.solve(docs, word))
