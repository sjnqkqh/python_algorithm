def twoSum(nums: list[int], target: int) -> list[int]:
    num_dict = dict()
    for i in range(len(nums)):
        if not num_dict.get(nums[i]):
            num_dict[nums[i]] = [i]
        else:
            num_dict.get(nums[i]).append(i)

    for k, v in num_dict.items():
        if k * 2 == target and len(v) > 1:
            return [v[0], v[1]]

        temp = v.pop()
        if num_dict.get(target - k) is not None and num_dict.get(target - k) != []:
            return [temp, num_dict.get(target - k)[0]]
        v.append(temp)


# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
