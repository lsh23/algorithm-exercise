if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N: int = int(input())
    employees: dict[str, str] = {}
    for _ in range(N):
        name: str
        log: str
        name, log = input().strip().split()
        employees[name] = log

    employees_in_company = [name for name in employees if employees[name] == "enter"]
    employees_in_company.sort(reverse=True)
    for name in employees_in_company:
        print(name)