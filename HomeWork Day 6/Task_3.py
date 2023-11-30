def caculatesum(a, x) -> int:
    '''
        This function to calculate sum
    '''
    return sum(a[0:x + 1])

def Input():
    '''
        This function to enter
    '''
    n = int(input("Enter n: "))
    a = [int(i) for i in input("Enter arrays of length n: ").split()]
    t = int(input("Enter t: "))
    for i in range(t):
        x = int(input("Enter x: "))
        print("Result = {}".format(caculatesum(a, x)))

Input()