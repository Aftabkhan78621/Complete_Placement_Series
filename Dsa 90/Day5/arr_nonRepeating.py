arr = [2,2,2,4,6,5,5,5,4,12,23]

freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

# find first non repeating element
for num in arr:
    if freq[num] == 1:
        print("first non repeating Element : ",num)
        break