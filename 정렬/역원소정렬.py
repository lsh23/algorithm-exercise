class Solution:
    def solve(self, elements: list[str]):
        elements = [ int("".join((list(e)[::-1]))) for e in elements]
        elements.sort()
        for e in elements:
            print(e)


if __name__ == '__main__':
    N: int
    elements: list[str] = []
    input_elements: list[str] = [x for x in input().split()]
    N = int(input_elements[0])
    elements += input_elements[1:]
    while True:
        try:
            input_elements = [x for x in input().split()]
            if input_elements:
                elements += input_elements
        except EOFError:
                break
    assert N == len(elements)
    s: Solution = Solution()
    s.solve(elements)
