def is_triangle_number(number: int) -> bool:
    if number == 1 or number == 0:
        return True
    for i in range(number):
        if number == (i*(i+1))/2:
            return True
    
    return False
    