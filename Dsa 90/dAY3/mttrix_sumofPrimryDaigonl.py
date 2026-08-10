matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diagonal_sum = 0
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]
print("Primary Daigonal Sum = ",diagonal_sum)

for i in range(len(matrix)):
    diagonal_sum += matrix[i][len(matrix)]
print("Primary Daigonal Sum = ",diagonal_sum)