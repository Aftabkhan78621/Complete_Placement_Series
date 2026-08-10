#     *
#    ***
#   *****
#  *******
# *********

# n = int(input("Enter a number: "))
# for i in range(n):
#     # print saces
#     for j in range(n-i-1):
#         print(' ',end='')
#     # print star
#     for j in range(2*i + 1):
#         print('*',end='')
#     print()

# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Enter n: "))

for i in range(n):

    # spaces
    for j in range(i):
        print(" ", end="")

    # stars
    for j in range(2 * (n - i) - 1):
        print("*", end="")

    print()

for i in range(5,0,-1):
    for j in range(5-i):
        print('  ',end='')
    for j in range(2*i - 1):
        print("*", end=' ')
    print()