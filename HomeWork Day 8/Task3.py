import numpy as np

class Matrix:
    def __init__(self, n=0, m=0):
        self.__n = n
        self.__m = m
        self.__matrix = np.zeros((n, m))
        print("Enter matrix: ")
        for i in range(n):
            for j in range(m):
                print(f"Enter matrix [{i}][{j}] = ", end="")
                x = float(input()) 
                self.__matrix[i][j] = x
    
    def __str__(self):
        print("Matrix: ")
        for i in range(self.__n):
            for j in range(self.__m):
                print(self.__matrix[i][j], end=" ")
            print("")
        return ""
    
    def __add__(self, other):
        new_matrix = np.add(self.__matrix, other.__matrix)
        return new_matrix
    
    def __sub__(self, other):
        new_matrix = np.subtract(self.__matrix, other.__matrix)
        return new_matrix
    
    def __mul__(self, other):
        new_matrix = np.multiply(self.__matrix, other.__matrix)
        return new_matrix
    
    def __truediv__(self, other):
        new_matrix = np.divide(self.__matrix, other.__matrix, out=np.zeros_like(self.__matrix), where=other.__matrix != 0)
        return new_matrix

    def __eq__(self, other):
        new_matrix = np.equal(self.__matrix, other.__matrix)
        if(new_matrix[0][0] == False): return False
        return True

a = Matrix(3, 3)
b = Matrix(3, 3)

print("a + b:")
print(a + b)

print("\na - b:")
print(a - b)

print("\na * b:")
print(a * b)

print("\na / b:")
print(a / b)

print("\na == b:")
print(a == b)
