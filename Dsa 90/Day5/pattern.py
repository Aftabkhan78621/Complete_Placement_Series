#  triangle type

n = int(input("Enter a number: "))
for i in range(1,n+1):
#    print space
    for j in range(n-i):
        print(' ',end='')
    #  print  numbers
    for j in range(1,i+1):
        print(j,end='')
    print()