def maximum_consecutive_ones(arr):

    count = 0
    maximum = 0

    for num in arr:

        if num == 1:
            count += 1
            maximum = max(maximum, count)

        else:
            count = 0

    return maximum


print(maximum_consecutive_ones([1,1,0,1,1,1]))      # 3
print(maximum_consecutive_ones([1,1,1,1]))          # 4
print(maximum_consecutive_ones([0,0,0]))            # 0
print(maximum_consecutive_ones([1,0,1,1,0,1]))      # 2


def one_edit_away(s1, s2):

    n = len(s1)
    m = len(s2)

    # Length difference more than 1
    if abs(n - m) > 1:
        return False

    # -----------------------------
    # Case 1: Same Length (Replace)
    # -----------------------------
    if n == m:

        diff = 0

        for i in range(n):

            if s1[i] != s2[i]:
                diff += 1

            if diff > 1:
                return False

        return diff == 1

    # -------------------------------------
    # Case 2: Length differs by 1
    # (Insert / Delete)
    # -------------------------------------

    # Make s1 the shorter string
    if n > m:
        s1, s2 = s2, s1
        n, m = m, n

    i = 0
    j = 0
    diff = 0

    while i < n and j < m:

        if s1[i] == s2[j]:
            i += 1
            j += 1

        else:
            diff += 1

            if diff > 1:
                return False

            # Skip one character in longer string
            j += 1

    return True


print(one_edit_away("cat", "cut"))     # True
print(one_edit_away("cat", "cart"))    # True
print(one_edit_away("cart", "cat"))    # True
print(one_edit_away("cat", "dog"))     # False
print(one_edit_away("abc", "abc"))     # False
print(one_edit_away("abc", "abdc"))    # True   

def pattern(n):

    for i in range(n):

        ch = chr(ord('A') + i)

        for j in range(i + 1):
            print(ch, end=" ")

        print()


pattern(5)


def first_unique(arr):

    frequency = {}

    # Count frequency
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    # Find first unique element
    for num in arr:

        if frequency[num] == 1:
            return num

    return -1


print(first_unique([4,5,1,2,0,4]))     # 5
print(first_unique([1,2,2,1]))         # -1
print(first_unique([7,7,8,9,9]))       # 8


def second_highest_frequency(arr):

    frequency = {}

    # Count frequency
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    first = float("-inf")
    second = float("-inf")

    # Find first and second highest frequencies
    for freq in frequency.values():

        if freq > first:
            second = first
            first = freq

        elif first > freq > second:
            second = freq

    if second == float("-inf"):
        return -1

    # Return first element having second highest frequency
    for num in arr:

        if frequency[num] == second:
            return num

    return -1


print(second_highest_frequency([1,2,2,3,3,3,4,4]))   # 2




def pattern(n):

    for i in range(1, n + 1):

        # Print spaces
        for j in range(n - i):
            print("  ", end="")

        # Print numbers
        for j in range(i, 0, -1):
            print(j, end=" ")

        print()


pattern(5)

def anagram_palindrome(text):

    frequency = {}

    # Count frequency
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    odd = 0

    # Count odd frequencies
    for freq in frequency.values():

        if freq % 2 != 0:
            odd += 1

    return odd <= 1


print(anagram_palindrome("carrace"))   # True
print(anagram_palindrome("daily"))     # False
print(anagram_palindrome("aabb"))      # True
print(anagram_palindrome("abc"))       # False