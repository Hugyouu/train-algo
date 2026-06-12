def isPalindrome(s: str) -> bool:
    s = "".join(filter(str.isalnum, s))
    s = list(s.lower())
    tab_bool = [False] * len(s)
    for i, c in enumerate(s):
        if c == s[len(s) - i - 1]:
            tab_bool[i] = True
    return tab_bool.count(True) == len(s)


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
