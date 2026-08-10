# # 1 2 3 5 6
# # missing number is = 4

# def missingNumber():
#     arr = [1,2,4,5,6]
#     a  = len(arr)

#     expected-sum = (n * (n + 1)) // 2

n = 5
# print( n * (n +1) //2 )

arr = [1, 2, 3, 5, 6]

n = len(arr) + 1

expected_sum = n * (n + 1) // 2

actual_sum = sum(arr)

print(expected_sum)
