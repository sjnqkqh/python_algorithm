from collections import deque


def make_cases(k):
    cases = []

    def make(text, max_len):
        if len(text) == max_len:
            cases.append(text)
            return

        if text[-1] == 'A':
            make(text + 'B', max_len)
            make(text + 'C', max_len)
        elif text[-1] == 'B':
            make(text + 'A', max_len)
            make(text + 'C', max_len)
        else:
            make(text + 'A', max_len)
            make(text + 'B', max_len)

    make('A', k)
    make('B', k)
    make('C', k)

    return cases


def num_to_char(i):
    if i == 1:
        return 'A'
    elif i == 2:
        return 'B'
    else:
        return 'C'


def contaminate_all_connected(graph, type, now, infected, infected_queue):
    for next_node in graph[(now, type)]:
        if not infected[next_node]:
            infected[next_node] = True
            infected_queue.append(next_node)
            contaminate_all_connected(graph, type, next_node, infected, infected_queue)


def make_infection_graph(n, edges):
    graph = dict()

    for i in range(1, n + 1):
        for j in ['A', 'B', 'C']:
            graph[(i, j)] = set()

    for i, j, type in edges:
        graph[(i, num_to_char(type))].add(j)
        graph[(j, num_to_char(type))].add(i)

    return graph


def solution(n, infection, edges, k):
    answer = 0
    graph = make_infection_graph(n, edges)
    cases = make_cases(k)
    for case in cases:
        infected = [False] * (n + 1)
        infected[infection] = True
        infected_queue = deque([infection])
        step_queue = deque(case)
        
        while step_queue:
            type = step_queue.popleft()
            while infected_queue:
                now = infected_queue.popleft()
                contaminate_all_connected(graph, type, now, infected, infected_queue)

            infected_queue = deque([i for i, is_infected in enumerate(infected) if is_infected])

        answer = max(answer, sum(infected))

    return answer
