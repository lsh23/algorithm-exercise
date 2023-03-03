if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    N: int
    M: int
    N, M = map(int, input().split())

    number_to_name: dict[str, str] = {}
    name_to_number: dict[str, str] = {}

    for i in range(1,N+1):
        name: str = input().strip()
        number_to_name[str(i)] = name
        name_to_number[name] = str(i)

    for _ in range(M):
        q: str = input().strip()
        if q in number_to_name:
            print(number_to_name[q])
        if q in name_to_number:
            print(name_to_number[q])

