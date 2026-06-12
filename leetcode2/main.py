def bookseller(stock) -> str:
    result = {"A": 0, "B": 0, "C": 0, "W": 0}
    for x in stock:
        cat = x.split()[0][0]
        if cat in result.keys():
            result[cat] += int(x.split()[1])
    return result

def deadfish_parser(string) -> list:
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

def missing_term(sequence: list) -> int:
    return 


if __name__ == "__main__":
    # print(bookseller(["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]))
    print(deadfish_parser("iiisdsdddddis"))
    