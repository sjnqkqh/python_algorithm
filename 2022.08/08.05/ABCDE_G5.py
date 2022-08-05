N, M = map(int, input().split())
arr = [[] for _ in range(N)]
visited = [False for _ in range(N)]
result = False

# 서로 연결되어 있는 친구 쌍 입력
for _ in range(M):
    person_1, person_2 = map(int, input().split())
    arr[person_1].append(person_2)
    arr[person_2].append(person_1)


# DFS 탐색 시작
def dfs(person_idx: int, link_cnt):
    # 연결이 5개 이상일 경우
    if link_cnt == 5:
        return True

    # 이동 가능한 친구
    friends = arr[person_idx]
    for friend in friends:
        if not visited[friend]:
            # 방문한 적 없는 친구에게 방문 이후 복귀 (백트래킹)
            visited[friend] = True

            # 만약 연결된 친구가 5명이 충족되면, 그대로 return True
            if dfs(friend, link_cnt + 1):
                return True
            visited[friend] = False

    # 방문할 수 있는 모든 경우를 순회하고 연결이 5이하인 경우, Return False
    return False


for item in range(N):
    visited[item] = True
    result = dfs(item, 1)
    visited[item] = False

    if result:
        print(1)
        break

# 끝내 연결된 친구가 5명이 되지 않았다면 print(0)
if not result:
    print(0)
