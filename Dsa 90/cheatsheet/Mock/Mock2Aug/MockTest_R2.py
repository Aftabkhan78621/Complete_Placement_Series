def longest_consecutive(arr):

    numbers = set(arr)

    maximum = 0

    for num in numbers:

        if num - 1 not in numbers:

            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            maximum = max(maximum, length)

    return maximum


print(longest_consecutive([100,4,200,1,3,2]))   # 4

def consecutive(arr):

    if len(arr) == 0:
        return 0

    sorte = sorted(arr)

    count = 1
    maximum = 1

    for r in range(1, len(sorte)):

        # Ignore duplicates
        if sorte[r] == sorte[r - 1]:
            continue

        # Consecutive
        elif sorte[r] - sorte[r - 1] == 1:
            count += 1
            maximum = max(maximum, count)

        # Sequence breaks
        else:
            count = 1

    return maximum


print(consecutive([100,4,200,1,3,2]))      # 4
print(consecutive([1,2,2,3]))              # 3
print(consecutive([1,3,5]))                # 1
print(consecutive([1,2,3,4,5]))            # 5

