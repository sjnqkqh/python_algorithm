def solution(nums: list):
    max_len = len(nums) // 2
    mon_set = set(nums)

    return min(max_len, len(mon_set))
