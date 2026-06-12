def find_duplicates(values: list) -> list:
    return list(set(x for x in values if values.count(x) > 1))


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 5, 1]))
