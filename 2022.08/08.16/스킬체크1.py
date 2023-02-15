def solution(routes):
    answer = 0

    while routes:
        route_dict = dict()
        for route in routes:
            for i in range(route[0], route[1] + 1):
                if route_dict.get(i) is None:
                    route_dict[i] = 1
                else:
                    route_dict[i] = route_dict.get(i) + 1

        choose = sorted(route_dict.items(), key=lambda x: -x[1])[0][0]
        answer += 1

        # 경로 상에 감시 카메라가 있으면 해당 경로는 선정에서 제외
        temp = []
        for route in routes:
            if route[0] <= choose <= route[1]:
                pass
            else:
                temp.append(route)
        routes = temp

        if len(routes) == 0:
            return answer
