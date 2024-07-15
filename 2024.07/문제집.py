import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

block_number_dict = {}  # 각 문제가 어떤 문제를 가로막고 있는지 List로 저장
block_count_dict = {}  # 각 문제를 풀기 위해 몇 개의 문제가 선행되는지 저장
priority_arr = []  # 모든 문제가 풀려서 정렬될 Array
result = []  # 최종 제출용 Array

for i in range(1, n + 1):
    block_number_dict[i] = []
    block_count_dict[i] = 0

for _ in range(m):
    a, b = map(int, input().split())  # B를 풀기위해 A가 선행된다.
    block_number_dict[a].append(b)
    block_count_dict[b] += 1

for k, v in block_count_dict.items():  # 문제의 입력이 세팅된 직후, 선행되는 문제가 없는 문제들은 즉시 prority_arr에 삽입한다.
    if v == 0:
        heapq.heappush(priority_arr, k)

while priority_arr:
    min_node = heapq.heappop(priority_arr)  # 풀 수 있는 문제 중 가장 난이도가 낮은 문제를 푼다.
    result.append(min_node)
    for blocked_number in block_number_dict.get(min_node):  # 이번에 풀린 문제가 막고 있던 문제들의 카운트를 감소시킨다.
        block_count_dict[blocked_number] -= 1
        if block_count_dict[blocked_number] == 0:  # 더 이상 가로막는 문제가 없다면, 해당 문제를 prority_arr에 삽입한다.
            heapq.heappush(priority_arr, blocked_number)

print(*result, sep=' ')
