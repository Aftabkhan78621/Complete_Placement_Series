print('hello world')
for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()

a = int(input('Enter a number: '))
for i in range(a):
    for j in range(i):
        print('*',end=' ')
    print()


for i in range(5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
