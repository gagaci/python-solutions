from collections import Counter

# https://algo.monster/problems/sliding_window_maximum
# https://algo.monster/liteproblems/3

def lengthOfLongestSubstring(s: str) -> int:
    # counter to track character frequencies in current window
    char_counter = Counter()

    # we keep length
    max_length = 0
    left = 0

    # we iterate through with right, enumerate help us to iterate with index-value pair
    for right, char in enumerate(s):
        # we add every char, to char_counter
        char_counter[char] += 1
        # if we encounter duplicate
        while char_counter[char] > 1:
           # we
           char_counter[s[left]] -= 1
           left += 1
        max_length = max(max_length, right - left + 1)
    return max_length



print(lengthOfLongestSubstring("abcabcbb"))
