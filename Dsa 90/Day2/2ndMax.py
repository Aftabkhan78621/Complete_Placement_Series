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


def secondMax(a):
    f = float('-inf')
    s = float('-inf')
    for no in a:
        if no > f:
            s = f
            f = no
        elif no > s and no != f:
            s = no
    return f,s

first,second = secondMax([1,2,3,7,9,80])
print("first is : ",first)
print("Second is : ",second)


def secondMax(a):
    f = float('inf')
    s = float('inf')
    for no in a:
        if no < f:
            s = f
            f = no
        elif no < s and no != f:
            s = no
    return f,s

first,second = secondMax([1,-20,3,7,9,80])
print("first is : ",first)
print("Second is : ",second)