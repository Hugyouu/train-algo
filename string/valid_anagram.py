# Given two strings s and t, return true if t is an of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): 
        return False
    for i in range(len(t)-1, -1, -1):
        if s.count(t[i]) == t.count(t[i]):
            continue
        else:
            return False
    return True

print(isAnagram("aacc", "ccac"))