#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumTreePath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER_ARRAY visitNodes
#
from collections import deque


def minimumTreePath(n, edges, visitNodes):
    result = 0
    arr = [[] for _ in range(n + 1)]
    for item in edges:
        arr[item[0]].append(item[1])
        arr[item[1]].append(item[0])

    search_start = 1
    while True:
        search_result = dfs([False for _ in range(n + 1)], search_start, arr, visitNodes, n)
        if search_result[0] == 'Finished':
            result += search_result[1]
            return result
        else:
            result += search_result[1]
            search_start = search_result[0]
            visitNodes.remove(search_result[0])


# BFS 탐색
def dfs(visited, start, arr, visitNodes, n):
    step = 0
    queue = deque()
    queue.append(start)

    while queue:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()

            # 방문 해야할 모든 노드를 거쳐서 마지막 노드에 도달하면 종료
            if len(visitNodes) == 0 and now == n:
                return 'Finished', step

            # 방문 해야 할 노드 중 가장 가까운 노드에 도달하면 해당 탐색 종료
            if now in visitNodes:
                return now, step

            # 방문 가능한 노드 중, 이번 탐색에서 방문하지 않은 노드는 큐에 넣음
            can_visit = arr[now]
            for point in can_visit:
                if not visited[point]:
                    visited[point] = True
                    queue.append(point)

        # 노드 간 거리 계산
        step += 1


import threading

threading.stack_size(10 ** 8)


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    edges_rows = int(input().strip())
    edges_columns = int(input().strip())

    edges = []

    for _ in range(edges_rows):
        edges.append(list(map(int, input().rstrip().split())))

    visitNodes_count = int(input().strip())

    visitNodes = []

    for _ in range(visitNodes_count):
        visitNodes_item = int(input().strip())
        visitNodes.append(visitNodes_item)

    result = minimumTreePath(n, edges, visitNodes)

    fptr.write(str(result) + '\n')

    fptr.close()


t = threading.Thread(target=main)
t.start()
t.join()
