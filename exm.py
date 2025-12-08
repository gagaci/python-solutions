def twoSum(nums, target):
    i = 0
    j = len(nums) - 1
    result = []
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            result.append(i)
            result.append(j)
            break
        elif s < target or i < len(nums) - 2:
            i += 1
        else:
            j -= 1
    return result



print(twoSum([3,2,4],6))