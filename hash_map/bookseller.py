def bookseller(stock) -> str:
    result = {"A": 0, "B": 0, "C": 0, "W": 0}
    for x in stock:
        cat = x.split()[0][0]
        if cat in result.keys():
            result[cat] += int(x.split()[1])
    return result


if __name__ == "__main__":
    print(bookseller(["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]))
