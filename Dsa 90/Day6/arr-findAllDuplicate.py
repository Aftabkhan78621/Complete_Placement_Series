# arr = [1,2,2,2,3,3,3,4,5,6,7,8]
# freq = {}
# result = []

# for num in arr:
#     if num in freq:
#         freq[num] +=1
#         result.append(num)
#     else:
#         freq[num] = 1
# print('duplicate element: ',freq)
# print('duplicates : ',result)


# for key in freq:
#     if freq[key] > 1:
#         print(key, end=" ")


# # find unique element
# arr = [1, 2, 3, 2, 4, 5, 3, 6]

# freq = {}

# for num in arr:
#     freq[num] = freq.get(num, 0) + 1

# for num in arr:
#     if freq[num] == 1:
#         print(num, end=" ")

# # 2. Print Duplicate Count
# arr = [1, 2, 3, 2, 4, 5, 3, 6]
# freq = {}
# results = []

# for num in arr:
#     freq[num] = freq.get(num,0) + 1
# for key in freq:
#     if freq[key] > 1:
#         print(key,'->',freq[key])


# # 3. Find Element with Maximum Frequency
# arr = [1, 2, 2, 3, 3, 3, 4,9,0,12,234]
# freq = {}
# for num in arr:
#     freq[num] = freq.get(num, 0) + 1
# max_count = 0
# answer = None
# for key in freq:
#     if freq[key] > max_count:
#         max_count = freq[key]
#         answer = key

# print(answer)


# 4. First Repeating Element
arr = [1, 2, 3, 2, 4, 5, 3]

seen = {}

for num in arr:
   if num in seen:
      print(num)
      break
   seen[num] = 1

# 5. First Non-Repeating Element
arr = [2, 3, 4, 2, 3, 5, 4]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] == 1:
        print(num)
        break


#     | Question            | Dictionary Condition    |
# | ------------------- | ----------------------- |
# | Unique Elements     | `freq[num] == 1`        |
# | Duplicate Elements  | `freq[num] > 1`         |
# | Duplicate Count     | `print(key, freq[key])` |
# | Maximum Frequency   | `freq[key] > max_count` |
# | First Repeating     | `if num in seen`        |
# | First Non-Repeating | `freq[num] == 1`        |

# 🎯 Interview Trick

# Jab bhi question me ye words dikhen:

# Frequency
# Count
# Duplicate
# Unique
# Occurrence
# Repeating
# Non-Repeating

# ➡️ Seedha Dictionary (HashMap) ke baare me socho.
