def is_include_vowels(password: str) -> bool:
    for c in password:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            return True
    return False


def is_three_sequence(password: str) -> bool:
    vowels_sequence_cnt: int = 0
    consonants_sequence_cnt: int = 0
    for c in password:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            consonants_sequence_cnt = 0
            vowels_sequence_cnt += 1
        else:
            vowels_sequence_cnt = 0
            consonants_sequence_cnt += 1
        if consonants_sequence_cnt >= 3 or vowels_sequence_cnt >= 3:
            return True
    return False


def is_two_sequence(pasword: str) -> bool:
    prev_c: str = ''
    for c in password:
        if prev_c != c:
            sequence_cnt = 1
            prev_c = c
        else:
            if c == 'e' or c == 'o':
                continue
            else:
                return True
    return False


class Solution:
    @staticmethod
    def solve(password: str) -> None:
        if not is_include_vowels(password):
            print(f'<{password}> is not acceptable.')
            return

        if is_three_sequence(password):
            print(f'<{password}> is not acceptable.')
            return

        if is_two_sequence(password):
            print(f'<{password}> is not acceptable.')
            return

        print(f'<{password}> is acceptable.')


if __name__ == "__main__":
    while True:
        password: str = input()
        if password == 'end':
            break
        Solution.solve(password)
