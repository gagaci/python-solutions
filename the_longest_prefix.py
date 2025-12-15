def longestCommonPrefix(words: list) -> str:
    # get use the shortest str to compare with other elements,
    # logically the shortest element is valid one to start
    short = min(words, key=len)
    m = len(short)
    prefix = ""
    # we iterate through i element of 'short' variable
    for i in range(m):
        for word in words:
            # then, we compare it short[i] with word[i],
            # if the condition is met, then we continue, if not we return prefix
            if short[i] != word[i]:
                return prefix
        # GGG: this the most important code in this solution, if short[i] and word[i] are equal,
        # we assign all chars until i + 1 to the prefix by short[:i+1] 
        prefix = short[:i+1]
    return short

print(longestCommonPrefix(["flower","flow","flight"]))

def longestCommonPrefixV2(words: list) -> str:
    short = min(words, key=len)
    m = len(short)
    prefix = ""
    for i in range(m):
        for word in words:
            if short[i] != word[i]:
                return word[:prefix]
        prefix = i+1
    return ""


print(longestCommonPrefix(["flower","flow","flight"]))





