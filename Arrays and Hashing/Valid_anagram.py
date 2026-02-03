from collections import Counter
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count_s = Counter(s)
    count_t = Counter(t)
    return count_s == count_t