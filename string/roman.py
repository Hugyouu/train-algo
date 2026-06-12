# I=1  V=5  X=10  L=50  C=100  D=500  M=1000

def solution(roman: str) -> int:
    values = []
    for letter in roman:
        match letter:
            case "I": values.append(1)
            case "V": values.append(5)
            case "X": values.append(10)
            case "L": values.append(50)
            case "C": values.append(100)
            case "D": values.append(500)
            case "M": values.append(1000)

    for index, value in enumerate(values):
        pass
    return values


if __name__ == "__main__":
    print(solution("MDCLXVI"))
    print(solution("MMMCMXCIX"))
