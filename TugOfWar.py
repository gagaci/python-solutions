def leftRightDifference(nums: list) -> list:
    total = sum(nums)
    left_sum = 0
    result = []
    for x in nums:
        right_sum = total - left_sum
        if right_sum < left_sum:
            result.append(-1)
        elif left_sum < right_sum:
            result.append(1)

        left_sum += x

    return result


print(leftRightDifference([1, 2, 3, 4]))
