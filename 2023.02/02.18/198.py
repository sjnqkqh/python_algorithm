def get_binary_sum(min_cut, max_cut):
    sum = 0
    cut_line = (min_cut + max_cut) // 2
    for item in arr:
        if item > cut_line :
            sum += (item - cut_line)
    
    if sum == m or min_cut == max_cut:
        print(cut_line)
        return
    elif sum < m:
        get_binary_sum(min_cut, cut_line)
    elif sum > m:
        get_binary_sum(cut_line+1, max_cut)
        
    
n,m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

get_binary_sum(0,arr[len(arr)-1])
