# 1
# 12
# 123
# 1234
# 12345

# n = int(input('Enter a number: '))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

for i in range(1,5):
    for j in range(1,i):
        print(j,end='')
    print()

for i in range(1,5):
    for j in range(1,i):
        print(i,end='')
    print()