text = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(text)):

    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)

print(result)

results = ''
counts = 1

# for i in range(1,len(text)):     # 1,5 
#     if text[i] == text[i - 1]:   # hello
#         count += 1
#     else:
#         results += text[i-1] + str(counts)
#         counts = 1
# result += text[-1] + str(counts)
# print(results)

# tc = o(n)
# sc = o(n)