# Input:
# [10,15,8,7,20]

# Output:
# Even = 3
# Odd = 2

n = [10,20,30,5,4,6]
even_cont = 0
odd_cont = 0
even_result = []
for num in n:
    if num % 2 == 0:
        even_cont += 1
        even_result.append(num)
    else:
        odd_cont += 1
print('Even = ',even_cont,even_result)
print('odd = ',odd_cont)