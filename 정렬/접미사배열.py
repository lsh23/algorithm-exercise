if __name__ == "__main__":
    S: str = input()
    s_postfix_list = [S[i:]for i in range(len(S))]
    assert len(S) == len(s_postfix_list)

    s_postfix_list.sort()

    for postfix in s_postfix_list:
        print(postfix)
