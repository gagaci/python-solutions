def longestCommonPrefix(words: list) -> str:
    short = min(words, key=len)
    m = len(short)
    prefix = ""
    for i in range(m):
        for word in words:
            if short[i] != word[i]:
                return prefix
        prefix = short[:i+1]
    return short


print(longestCommonPrefix(["flower","flow","flight"]))





