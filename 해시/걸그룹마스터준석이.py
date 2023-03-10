if __name__ == '__main__':
    N: int
    M: int
    N, M = map(int, input().split())
    group_to_member: dict[str, list[str]] = {}
    member_to_group: dict[str, str] = {}
    for _ in range(N):
        g_name: str = input()
        g_number: int = int(input())
        for _ in range(g_number):
            member: str = input()
            if g_name in group_to_member:
                group_to_member[g_name].append(member)
            else:
                group_to_member[g_name] = [member]
            member_to_group[member] = g_name
    for _ in range(M):
        p: str = input()
        p_flag: int = int(input())
        if p_flag == 0:
            for m in sorted(group_to_member[p]):
                print(m)
        else:
            print(member_to_group[p])

