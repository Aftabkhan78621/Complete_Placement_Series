# Input:
# "I Love Python"

# Output:
# ILovePython

# s = input('Enter a string: ')
# result = ''
# for ch in s:
#     if ch!=' ':
#         result += ch
# print(result)


def spaceing(s):
    res = ''
    for ch in s:
        if ch != " ":
            res+= ch
    return res
print(spaceing("i love python "))