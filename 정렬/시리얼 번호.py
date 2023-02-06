from __future__ import annotations


class SerialNumber:
    def __init__(self, serial_number: str):
        self.value = serial_number

    def get_sum_of_digits(self) -> int:

        sum_of_digits: int = 0
        for x in self.value:
            if x.isdigit():
                sum_of_digits += int(x)
        return sum_of_digits

    def __lt__(self, other: SerialNumber):
        if len(self.value) != len(other.value):
            return len(self.value) < len(other.value)
        if self.get_sum_of_digits() != other.get_sum_of_digits():
            return self.get_sum_of_digits() < other.get_sum_of_digits()
        return self.value < other.value


class Solution:
    def solve(self, n: int, serial_numbers: list[SerialNumber]):
        serial_numbers.sort()
        for x in serial_numbers:
            print(x.value)


if __name__ == '__main__':
    N: int = int(input())
    serial_numbers: list(SerialNumber) = [SerialNumber(input()) for i in range(N)]
    s: Solution = Solution()
    s.solve(N, serial_numbers)