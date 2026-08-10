a = [1,31,44,5]
largest = a[0]
for num in a:
    if num > largest:
        largest = num
print('Max number is: ',largest)

for num in a:
    if num < largest:
        largest = num
print('min num is: ',largest)


print(max(a))
print(min(a))