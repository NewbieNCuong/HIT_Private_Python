def MyMultiple(*args) -> float:
    '''
        This function return a multiple of numbers
    '''
    sum = 1
    for i in args:
        sum *= i
    return sum

print("{:.1f}".format(MyMultiple(1, 2, 3, 4)))
print("{:.1f}".format(MyMultiple(5, 5, 5)))
print("{:.1f}".format(MyMultiple(1.2, 5)))