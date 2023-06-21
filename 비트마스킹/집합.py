if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    M: int
    M = int(input())
    s = 0
    for _ in range(M):
        command: list[str] = input().split()
        if len(command) == 1:
            if command[0] == "all":
                for i in range(1, 21):
                    s = (1 << 21) - 1
            elif command[0] == "empty":
                s = 0
        else:
            if command[0] == "add":
                s |= (1 << int(command[1]))
            elif command[0] == "remove":
                s &= ~(1 << int(command[1]))
            elif command[0] == "check":
                if s & (1 << int(command[1])):
                    print(1)
                else:
                    print(0)
            elif command[0] == "toggle":
                s ^= (1 << int(command[1]))
