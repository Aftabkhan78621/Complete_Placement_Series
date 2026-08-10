# # 1 2 3
# # 4 5 6
# # 7 8 9

# Column 1 = 12
# Column 2 = 15
# Column 3 = 18

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for j in range(cols):

    column_sum = 0

    for i in range(rows):
        column_sum += matrix[i][j]

    print(f"Column {j + 1} = {column_sum}")