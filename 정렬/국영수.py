class Student:
    def __init__(self, name: str, k: str, e: str, m: str):
        self.name = name
        self.k = int(k)
        self.e = int(e)
        self.m = int(m)
    def __lt__(self, other):
        if self.k != other.k:
            return self.k > other.k
        if self.e != other.e:
            return self.e < other.e
        if self.m != other.m:
            return self.m > other.m
        return self.name < other.name


class Solution:
    def solve(self, students: list[Student]):
        students.sort()
        for s in students:
            print(s.name)


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    N: int = int(input())
    students: list[Student]= []
    for _ in range(N):
        name, k, e, m = input().strip().split()
        students.append(Student(name, k, e, m))
    s: Solution = Solution()
    s.solve(students)