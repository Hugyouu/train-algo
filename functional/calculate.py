# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five()))    #  must return 35
# four(plus(nine()))      #  must return 13
# eight(minus(three()))   #  must return 5
# six(divided_by(two()))  #  must return 3

# Requirements:

#     There must be a function for each number from 0 ("zero") to 9 ("nine")
#     There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
#     Each calculation consist of exactly one operation and two numbers
#     The most outer function represents the left operand, the most inner function represents the right operand
#     Division should be integer division. For example, this should return 2, not 2.666666...:

# eight(divided_by(three()))


def zero(op=None):
    return op(0) if op else 0
def one(op=None):
    return op(1) if op else 1
def two(op=None):
    return op(2) if op else 2
def three(op=None):
    return op(3) if op else 3
def four(op=None):
    return op(4) if op else 4
def five(op=None):
    return op(5) if op else 5
def six(op=None):
    return op(6) if op else 6
def seven(op=None):
    return op(7) if op else 7
def eight(op=None):
    return op(8) if op else 8
def nine(op=None):
    return op(9) if op else 9

def plus(right): 
    return lambda left: left + right
def minus(right): 
    return lambda left: left - right
def times(right): 
    return lambda left: left * right
def divided_by(right): 
    return lambda left: left // right