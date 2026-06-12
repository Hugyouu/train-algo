def isValid(s: str) -> bool:
    import re
    s = "".join(filter(str.isalpha,s))
    tab_bool = [False]*len(s)
    dict = {'(':')', '[':']', '{':'}'}
    print(s)
    for i, x in enumerate(s):
        if bool(re.match(r"[\(\[\{\}\]\)]", x)):
            if dict[x] == s[len(s) - i - 1]:
                tab_bool[i] = True
    return all(tab_bool)
    
    
if __name__ == "__main__":
    print(isValid("([])"))