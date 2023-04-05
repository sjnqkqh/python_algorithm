arr = [['' for _ in range(3)] for _ in range(3)]
parent = [[] for _ in range(3)]
for i in range(3):
    for j in range(3):
        parent[i].append([i, j])


def find_parent(r1, c1):
    if parent[r1][c1] != [r1, c1]:
        parent[r1][c1] = find_parent(parent[r1][c1][0], parent[r1][c1][1])
    return parent[r1][c1]


def union(r1, c1, r2, c2):
    p_a = find_parent(r1, c1)
    p_b = find_parent(r2, c2)
    parent[p_b[0]][p_b[1]] = p_a

    for item in parent:
        print(item)
    print()



def solution(commands):
    answer = []

    for item in commands:
        if item.startswith("UPDATE"):
            l = item.split()
            if len(l) == 4:
                r, c, s = int(l[1]), int(l[2]), l[3]
                arr[r][c] = s
            else:
                before, after = l[1:]
        elif item.startswith("MERGE"):
            r1, c1, r2, c2 = map(int, item.split()[1:])
            if r1 != r2 or c1 != c2:
                union(r1, c1, r2, c2)
                # if arr[r1][c1][0] == '' and arr[r2][c2][0] != '':
                #     arr[r1][c1] = arr[r2][c2]
                # else:
                #     # arr[r1][c1][0] != '' and arr[r2][c2][0] == '' or arr[r1][c1][0] != '' and arr[r2][c2][0] != '':
                #     arr[r2][c2] = arr[r1][c1]

        elif item.startswith("UNMERGE"):
            r, c = map(int, item.split()[1:])
            # print(arr[r][c])
            # for r1, c1 in arr[r][c][1]:
            #     print(arr[r1][c1])
            #     arr[r1][c1][0] = ''
            #     arr[r1][c1][1].remove([r, c])
            #     print(r1, c1, arr[r1][c1])

        else:
            print(4)

    for item in arr[1:3]:
        print(item[1:3])

    return answer


solution(
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d",
     "MERGE 1 1 1 2",
     "MERGE 2 2 2 1",
     "MERGE 2 1 1 1",
     "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])
