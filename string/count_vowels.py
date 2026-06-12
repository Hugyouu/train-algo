import re


def count_vowels(word: str) -> int:
    return len([x for x in word if bool(re.match(r"\b[aeiouAEIOU]\b", x))])


if __name__ == "__main__":
    print(count_vowels("bonjour"))
