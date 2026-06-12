def longest_word(string: str) -> str:
    return max(string.split(), key=len)


if __name__ == "__main__":
    print(longest_word("bonjour je suis davit"))
