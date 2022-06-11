matrix1 = [
    [9, 0],
    [3, 6],
]

matrix2 = [
    [3, 2],
    [1, 5],
]

for x in range(0, len(matrix1)):
    for y in range(0, len(matrix1[0])):
        print(matrix1[x][y] + matrix2[x][y], end=' ',)
    print()