def in_range(word, start, end):
    start = start
    end = end
    for char in word:
        if not start <= ord(char) <= end:
            return False
    return True


def isupper(word):
    return in_range(word, 65, 90)

def islower(word):
    return in_range(word, 97, 122)

def detectCapitalUse(word: str) -> bool:
    if isupper(word) or islower(word):
        return True

    return isupper(word[:1]) and islower(word[1:])


print(detectCapitalUse("gerg"))

