def sorted_squares(nums: list) -> list:
    result = []
    for i in nums:
         result.append(i * i)
    result.sort()
    return result

print(sorted_squares([4, -1, 0, 3, 10]))
