# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    sorted_arr = sorted([x for x in source_array if x % 2 != 0], key=int, reverse=True)
    for i, n in enumerate(source_array):
        if len(sorted_arr) != 0 and n % 2 != 0:
            source_array[i] = sorted_arr.pop()
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))