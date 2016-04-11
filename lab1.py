""" Count the number of zero values in nXm dimansional array """
import random

def generateMatrix(n,m):
    matrix = [[random.randint(-5, 5) for i in range(n)] for i in range(m)]
    return matrix

def countZeroValues(matrix):
    counter = 0
    for row in matrix:
        for value in row:
            if value == 0:
                counter += 1
    return counter

if __name__ == '__main__':
    matrix = generateMatrix(6,5)
    print(matrix)
    counter = countZeroValues(matrix)
    print(counter)