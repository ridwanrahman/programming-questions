# 1. Swapping two number. (Using a third variable)
def swap_numbers_with_variable(a,b):
    c = b
    b = a
    a = c
    print (a,b)

# 2. Swapping two number. (Without using a third variable)
def swap_numbers_without_third_variable(a,b):
    a = a + b
    b = a - b
    a = a - b
    print (a,b)

swap_numbers_without_third_variable(3,4)