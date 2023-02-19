import sys

def binary_search(start, end, target):
    standard = spair_list[(start+end)//2]

    if start == end and target !=standard:
        print('no', end=" ")
        return
    
    if standard == target:
        print('yes', end =" ")
    elif standard > target:
        binary_search((start+end)//2+1, end, target)
    elif standard < target:
        binary_search(start, (start+end)//2-1, target)
        

n = int(input())
spair_list = sys.stdin.readline().rstrip().split(" ")
m = int(input())
search_list = sys.stdin.readline().rstrip().split(" ")
spair_list.sort()

for search in search_list:
    binary_search(0, n, search)
        
    