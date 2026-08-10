#  1. missing number

# def is_missing_Number(num):
#     l = len(num) + 1
#     expected_sum = l * (l + 1) // 2
#     actual_sum = sum(num)

#     return expected_sum - actual_sum


# def main():
#     num = [1,2,3,5]
#     missing = is_missing_Number(num)
#     if missing:
#         print("Missing number is : ",missing)
#     else:
#         print("no missing number")


# if __name__ == '__main__':
#     main()

# arr = [101, 101, 102, 103, 103, 104, 105, 105]

# if not arr:
#     print([])
# else:
#     write = 0

#     for read in range(1, len(arr)):
#         if arr[read] != arr[write]:
#             write += 1
#             arr[write] = arr[read]

#     for i in range(write + 1):
#         print(arr[i], end=" ")





# remove duplicates
def removeduplicates():
    arr = [11,1,1,1,3,2,2,2,4,5,6]
    seen = {}
    result = []
    
    for num in arr:
        if num not in seen:
            seen[num] = True
            result.append(num)
    return result
print(removeduplicates())
