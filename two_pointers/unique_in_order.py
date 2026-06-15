def unique_in_order(sequence):
    arr = []
    for s in sequence:
        if not arr or arr[-1] != s:
            arr.append(s)
    return arr

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('A'))
# unique_in_order('ABBCcAD')         
# unique_in_order([1, 2, 2, 3, 3])   
# unique_in_order((1, 2, 2, 3, 3))   
