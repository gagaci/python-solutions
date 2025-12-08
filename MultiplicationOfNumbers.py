def productExceptSelf(nums: list) -> list:
    prefix = [1]
    suffix = [1]
    product = 1
    for num in nums:
        product *= num
        prefix.append(product)

    product = 1
    for num in reversed(nums):
        product *= num
        suffix.append(product)

    print("prefix", prefix)
    print("suffix", suffix)


