def transposeMatrix(matrix):
    transposeMatrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposeMatrix.append(newRow)
    return transposeMatrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(transposeMatrix(matrix))