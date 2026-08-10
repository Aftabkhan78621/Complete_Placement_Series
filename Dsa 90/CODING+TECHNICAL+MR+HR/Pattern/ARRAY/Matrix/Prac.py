# def matrix_travese(matrix):
#     for row in matrix:
#         for value in row:
#             print(value,end=' ')
#         print()
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print("Matrix Traversal:")
# matrix_travese(matrix)

# def Row_sum(matrix):
#     result = []
#     for row in matrix:
#         total = 0
#         for value in row:
#             total += value
#         result.append(total)
#     return result
# print()

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print('Row Sum: ')
# print(Row_sum(matrix))


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [7,8,9]

# ]
# rows = len(matrix)
# cols = len(matrix[0])
# print(rows)
# print(cols)
# result = []

# for col in range(cols):
#   total = 0
#   for row in range(rows):
#    total += matrix[row][col]
#     result.append(total)
# print(result)



# def dia_sum(matrix):
#     total = 0
#     n = len(matrix)
#     for i in range(n):
#         total += matrix[i][n-i-1]
#     return total
# print()

# matrix = [
#     [1,2,13],
#     [4,5,6],
#     [7,8,9]
# ]
# print(len(matrix))

# print('dia Sum: ')
# print(dia_sum(matrix))def transpose_matrix(matrix):
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * rows for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            result[col][row] = matrix[row][col]

    return result


def rotate90(matrix):
    # Step 1: Transpose
    rotated = transpose_matrix(matrix)

    # Step 2: Reverse every row
    for row in rotated:
        row.reverse()

    return rotated


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTranspose:")
for row in transpose_matrix(matrix):
    print(row)

print("\n90° Clockwise Rotation:")
for row in rotate90(matrix):
    print(row)