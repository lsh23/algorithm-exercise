from itertools import combinations_with_replacement


def solution(n, info):
    answer = []
    max_diff = 0
    min_lion_point = 56
    for cwr in combinations_with_replacement([x for x in range(11)], n):
        result = [0] * 11
        lion_point = 0
        apeach_point = 0
        for x in cwr:
            result[10 - x] += 1
        for i in range(11):
            if info[i] == result[i] == 0:
                continue
            if info[i] < result[i]:
                lion_point += (10 - i)
            else:
                apeach_point += (10 - i)

        if lion_point <= apeach_point:
            continue

        diff = lion_point - apeach_point

        if diff > max_diff:
            answer = result
            max_diff = diff
            min_lion_point = lion_point
            continue

        if diff == max_diff:
            if min_lion_point > lion_point:
                for i in range(10, -1, -1):
                    if info[i] != result[i]:
                        if result[i] > info[i]:
                            answer = result
                            min_lion_point = lion_point
                        break

    if len(answer) == 0:
        return [-1]

    return answer
