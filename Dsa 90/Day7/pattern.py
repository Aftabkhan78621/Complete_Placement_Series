# 1
# 22
# 333
# 4444
# 55555

n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(i):
        print(i,end='')
    print()

for i in range(1,n+1):
    for j in range(1,i):
        print(j,end='')
    print()