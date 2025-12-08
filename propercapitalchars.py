def detectCapitalUse(word: str) -> bool:
    capital = word.isupper()
    is_lower = word.islower()
    is_first_char_capital = word.istitle()

    return capital or is_lower or is_first_char_capital


print(detectCapitalUse("USA"))