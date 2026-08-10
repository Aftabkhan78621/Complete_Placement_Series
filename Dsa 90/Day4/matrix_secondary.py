matrix = [
    [1,2,3],
    [4,10,6],
    [7,8,9]
]
n = len(matrix)
Secondary_diagonal_sum = 0
for i in range(n):
    Secondary_diagonal_sum += matrix[i][n-i-1]
print("Primary Daigonal Sum = ",Secondary_diagonal_sum)