if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    N: int
    M: int
    N, M = map(int, input().split())
    site_to_pw_map: dict[str, str] = {}
    for _ in range(N):
        site_url: str
        pw: str
        site_url, pw = input().strip().split()
        site_to_pw_map[site_url] = pw
    for _ in range(M):
        site_url: str
        site_url = input().strip()
        print(site_to_pw_map[site_url])