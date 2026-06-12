import re

def reverse_string(str) -> str:
    return str[::-1]

def count_vowels(word: str) -> int:
    return len([x for x in word if bool(re.match(r"\b[aeiouAEIOU]\b", x))])

def is_palindrome(word) -> bool:
    return word == word[::-1]

def find_max(int_list) -> int:
    return sorted(int_list)[-1]

def count_occurrences(tab: list, value) -> int:
    return len([x for x in tab if x == value])

def fizz_buzz(value) -> None:
    print(*("FizzBuzz" if (x%3==0 and x%5==0) else "Buzz" if x%5==0 else "Fizz" if x%3==0 else x for x in range(1, value+1)), sep="\n")

def valid_parentheses(string) -> bool:
    return all({'(':')', '[':']', '{':'}'}[c] == [x for x in string if bool(re.match(r"[\(\[\{\}\]\)]", x))][-i-1] for i, c in enumerate([x for x in string if re.match(r"[\(\[\{\}\]\)]", x)][:len([x for x in string if re.match(r"[\(\[\{\}\]\)]", x)])//2]))

def find_duplicates(values: list) -> list:
    return list(set(x for x in values if values.count(x) > 1))

# def longuest_word(string: str) -> str:
#     return [x for x in string.split()][[len(x) for x in [x for x in string.split()]].index(max([len(x) for x in [x for x in string.split()]]))]
def longuest_word(string: str) -> str:
    return max(string.split(), key=len)


# TODO
def two_sum(tab: list, value: int) -> tuple:
    seen = {}
    for i, n in enumerate(tab):
        if True:
            return (seen[i], i)
    
        indexes[value] = n



if __name__ == "__main__":
    # print(reverse_string("hello"))
    # print(count_vowels("bonjour"))
    # print(is_palindrome("kayask"))
    # print(find_max([3, 8, 2, 15, 4]))
    # print(count_occurrences([1, 2, 3, 2, 2, 4], 2))
    # fizz_buzz(100)
    # print(valid_parentheses("([{}])"))
    # print(find_duplicates([1, 2, 3, 2, 5, 1]))
    print(longuest_word("bonjour je suis davit"))
    pass