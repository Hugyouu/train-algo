
def duplicate_encode(word: str):
    arr = []
    for i in word.lower():
        if word.lower().count(i) != 1:
            arr.append(')')
        else:
            arr.append('(')
            
    return "".join(arr)

print(duplicate_encode("WSBJaCyYapRPl)"))