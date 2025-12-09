def longestCommonPrefix(words: list) -> str:
    short = min(words, key=len)
    m = len(short)
    prefix = ""
    for i in range(m):
        for word in words:
            if short[i] != word[i]:
                return prefix
        prefix = short[:i+1]
    return ""

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





