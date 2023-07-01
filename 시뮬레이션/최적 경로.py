def permutation(l, visited, result):
    global answer
    if l == N:
        prev_x = w_x
        prev_y = w_y
        dist = 0
        for i in range(N):
            # print(prev_x, prev_y)
            client_x = clients[result[i]][0]
            client_y = clients[result[i]][1]
            dist += abs(client_x - prev_x) + abs(client_y - prev_y)
            prev_x = client_x
            prev_y = client_y
        dist += abs(prev_x - h_x) + abs(prev_y - h_y)
        # print(result, dist)
        answer = min(dist, answer)
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                result[l] = i
                permutation(l + 1, visited, result)
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    w_x, w_y, h_x, h_y, *clients = map(int, input().split())
    clients = [(clients[i], clients[i + 1]) for i in range(0, 2 * N, 2)]
    answer = 10000
    permutation(0, [0] * N, [0] * N)
    print(f'#{test_case} {answer}')
