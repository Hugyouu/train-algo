def deadfish_parser(string: str) -> list:
    tab = []
    result = 0
    for i in string:
        if i == "i":
            result += 1
        elif i == "d":
            result -= 1
        elif i == "s":
            result *= result
        elif i == "o":
            tab.append(result)
    return tab


if __name__ == "__main__":
    print(deadfish_parser("iiisdsdddddis"))
