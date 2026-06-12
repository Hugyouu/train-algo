def count_occurrences(tab: list, value) -> int:
    return len([x for x in tab if x == value])


if __name__ == "__main__":
    print(count_occurrences([1, 2, 3, 2, 2, 4], 2))
