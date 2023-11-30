import numpy as np
def transpose(a) -> np.array:
    '''
        This function transposes
    '''
    return np.transpose(a)


n = int(input("Enter in rows: "))
m = int(input("Enter in columns: "))
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])

res = transpose(a)
print(res)