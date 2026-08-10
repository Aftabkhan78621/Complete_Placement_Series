arr = [10,20,5,8,15]
smallest = float('inf')
second_smallest = float('inf')

for num in arr:
    if num < smallest :
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
print("Second Smallet = ",second_smallest)




arr = [10, 20, 5, 7, 8, 40]

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)