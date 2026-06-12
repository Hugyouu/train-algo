def find_max(int_list: list) -> int:
    return sorted(int_list)[-1]


if __name__ == "__main__":
    print(find_max([3, 8, 2, 15, 4]))
