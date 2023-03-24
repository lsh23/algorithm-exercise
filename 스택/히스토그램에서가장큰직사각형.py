class Solution:
    def solve(self, n: int , heights: list[int]) -> int:

        ans: int = 0
        st: list[int] = [0]


        for i in range(n):

            while st and heights[st[-1]] > heights[i]:
                h = heights[st[-1]]

                left = -1
                right = i

                st.pop()
                if st:
                    left = st[-1]

                w = right - left - 1

                area = w * h
                ans = max(area, ans)

            st.append(i)

        while st:
            h = heights[st[-1]]

            left = -1
            right = n

            st.pop()
            if st:
                left = st[-1]
            w = right - left - 1

            area = w * h
            ans = max(area, ans)

        return ans


if __name__ == '__main__':
    while True:
        heights: list[int] = [int(x) for x in input().split()]

        if len(heights) == 1:
            break

        n: int = heights[0]
        heights = heights[1:]

        s: Solution = Solution()
        print(s.solve(n, heights))
