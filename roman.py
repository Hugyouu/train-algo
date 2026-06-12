# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000



def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    values = []
    for letter in roman: 
        match letter:
            case "I":
                values.append(1)
            case "V":
                values.append(5)
            case "X":
                values.append(10)
            case "L":
                values.append(50)
            case "C":
                values.append(100)
            case "D":
                values.append(500)
            case "M":
                values.append(1000)

    for index, value in enumerate(values):
        pass
    return values


if __name__ == "__main__":
    roman1 = "MDCLXVI"
    number1 = solution(roman1)
    print(f"La valeur de {roman1} est égale à {number1}")
    roman2 = "MMMCMXCIX"
    number2 = solution(roman2)
    print(f"La valeur de {roman2} est égale à {number2}")