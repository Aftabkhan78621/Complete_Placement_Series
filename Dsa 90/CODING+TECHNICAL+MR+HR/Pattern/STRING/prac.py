# def compare_string(a, b):
#     if a == b:
#         return "both are same"
#     elif a > b:
#         return "a is greater than b"
#     else:
#         return "b is greater than a"


# a = input("Enter first string: ")
# b = input("Enter second string: ")

# # print(compare_string(a, b))
# def sorting_string(text):
#     text = text.replace("", "")
#     return "".join(sorted(text))

# print(sorting_string("hello world"))

# def Larg_short(words):
#     return min(words),max(words)
# words = ['apple','banan','cat','dog','elephnt']
# print()
# print(Larg_short(words))


# def first_occr(text,pattern):
#     return text.find(pattern)
# print()
# print(first_occr("banaana",'ana'))

# def first_occr(text,pattern):
#     return text.rfind(pattern)
# print()
# print(first_occr("banaana",'ana'))


def count_pttern(t,p):
    n = len(t)
    m = len(p)
    count = 0
    for i in range(n-m+1):
        if t[i:i+m] == p:
            count += 1
    return count

print()
print(count_pttern("AABAACAADAABAABA", "AABA"))
