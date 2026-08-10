# ============================================================
# KADANE'S ALGORITHM PATTERN
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. MAXIMUM SUBARRAY SUM (Kadane's Algorithm)
# ============================================================

"""
THEORY (Interview Explanation)

Kadane's Algorithm ka use array me maximum sum wale continuous
subarray ko find karne ke liye hota hai. Har element par hum decide
karte hain ki current element se nayi subarray start kare ya previous
subarray ko continue kare. Agar previous sum negative ho jaye to usse
continue karne ka koi fayda nahi hota, isliye current element se naya
sum start karte hain. Isi wajah se algorithm sirf ek traversal me answer
nikal deta hai. Service-based companies me ye bahut famous interview
question hai.
"""

def maximum_subarray_sum(arr):

    current_sum = arr[0]

    maximum_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = max(arr[i], current_sum + arr[i])

        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


arr = [-2,1,-3,4,-1,2,1,-5,4]

print("Maximum Subarray Sum :", maximum_subarray_sum(arr))


# Complexity
# Time  : O(n)
# Space : O(1)



# ============================================================
# 2. MAXIMUM CIRCULAR SUBARRAY SUM
# ============================================================

"""
THEORY (Interview Explanation)

Circular Array me last element ke baad first element aata hai. Isliye
maximum subarray normal array ke andar bhi ho sakta hai aur end + start
ko mila kar bhi ban sakta hai. Is problem ko solve karne ke liye ek baar
normal Kadane chalate hain aur ek baar minimum subarray nikalte hain.
Total Sum - Minimum Subarray se circular answer mil jata hai. Fir dono
answers me maximum return kar dete hain.
"""

def maximum_circular_sum(arr):

    total = sum(arr)

    current_max = arr[0]
    max_sum = arr[0]

    current_min = arr[0]
    min_sum = arr[0]

    for i in range(1, len(arr)):

        current_max = max(arr[i], current_max + arr[i])
        max_sum = max(max_sum, current_max)

        current_min = min(arr[i], current_min + arr[i])
        min_sum = min(min_sum, current_min)

    if max_sum < 0:
        return max_sum

    return max(max_sum, total - min_sum)


arr = [5,-3,5]

print("Maximum Circular Sum :", maximum_circular_sum(arr))


# Complexity
# Time  : O(n)
# Space : O(1)



# ============================================================
# 3. MAXIMUM PRODUCT SUBARRAY
# ============================================================

"""
THEORY (Interview Explanation)

Product problems me negative numbers important hote hain. Do negative
numbers milkar positive product bana sakte hain, isliye sirf maximum
product rakhna kaafi nahi hota. Har step par maximum aur minimum dono
product maintain karte hain. Agar current number negative ho to maximum
aur minimum swap ho jate hain. Is approach se ek traversal me maximum
product subarray mil jata hai.
"""

def maximum_product_subarray(arr):

    maximum = arr[0]
    minimum = arr[0]

    answer = arr[0]

    for i in range(1, len(arr)):

        if arr[i] < 0:

            maximum, minimum = minimum, maximum

        maximum = max(arr[i], maximum * arr[i])

        minimum = min(arr[i], minimum * arr[i])

        answer = max(answer, maximum)

    return answer


arr = [2,3,-2,4]

print("Maximum Product Subarray :", maximum_product_subarray(arr))


# Complexity
# Time  : O(n)
# Space : O(1)


# ============================================================
# Expected Output
# ============================================================

# Maximum Subarray Sum :
# 6

# Maximum Circular Sum :
# 10

# Maximum Product Subarray :
# 6


# ============================================================
# INTERVIEW POINTS
# ============================================================

# Kadane Algorithm        O(n)
# Circular Kadane         O(n)
# Max Product             O(n)

# ============================================================
# KADANE PATTERN COMPLETE ✅
# ============================================================