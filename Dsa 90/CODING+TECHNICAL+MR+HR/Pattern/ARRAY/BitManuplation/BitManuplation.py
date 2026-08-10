# ============================================================
# BIT MANIPULATION PATTERN - Batch 1
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. CHECK ODD / EVEN
# ============================================================

"""
THEORY (Interview Explanation)

Har integer ka Least Significant Bit (LSB) decide karta hai ki number
odd hai ya even. Agar last bit 1 hai to number odd hota hai aur agar
last bit 0 hai to number even hota hai. Isliye modulo (%) use karne ki
jagah Bitwise AND (&) operator use karna fast aur efficient mana jata
hai. Expression (n & 1) last bit ko check karta hai. Ye Bit Manipulation
ka sabse basic concept hai aur interviews me frequently pucha jata hai.
"""

def check_odd_even(n):

    if n & 1:

        return "Odd"

    return "Even"


print("Odd / Even :")
print(check_odd_even(15))
print(check_odd_even(20))


# Time  : O(1)
# Space : O(1)



# ============================================================
# 2. CHECK POWER OF TWO
# ============================================================

"""
THEORY (Interview Explanation)

Power of 2 numbers (1, 2, 4, 8, 16...) ke binary representation me sirf
ek hi bit set hoti hai. Agar kisi number ka expression (n & (n-1))
zero aa jaye to matlab usme sirf ek set bit thi aur wo Power of Two hai.
Ye Bit Manipulation ka sabse famous trick hai aur TCS Prime me kaafi
popular interview question hai.
"""

def power_of_two(n):

    if n <= 0:

        return False

    return (n & (n - 1)) == 0


print()

print("Power Of Two :")
print(power_of_two(16))
print(power_of_two(18))


# Time  : O(1)
# Space : O(1)



# ============================================================
# 3. COUNT SET BITS
# ============================================================

"""
THEORY (Interview Explanation)

Set Bit ka matlab binary representation me 1 hota hai. Count Set Bits
problem me hume total number of 1s count karne hote hain. Har iteration
me last bit ko check karte hain aur right shift (>>) karke next bit par
chale jate hain. Ye Binary Numbers aur Bitwise Operators ko samajhne ka
important question hai. Interview me iska optimized version bhi pucha
ja sakta hai (Brian Kernighan Algorithm).
"""

def count_set_bits(n):

    count = 0

    while n > 0:

        count += (n & 1)

        n >>= 1

    return count


print()

print("Count Set Bits :")
print(count_set_bits(13))


# ============================================================
# Expected Output
# ============================================================

# Odd / Even :
# Odd
# Even

# Power Of Two :
# True
# False

# Count Set Bits :
# 3


# ============================================================
# Complexity
# ============================================================

# Check Odd / Even
# Time  : O(1)
# Space : O(1)

# Power Of Two
# Time  : O(1)
# Space : O(1)

# Count Set Bits
# Time  : O(log n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ n & 1          -> Check Odd / Even
# ✔ n & (n - 1)    -> Check Power of Two
# ✔ n >> 1         -> Right Shift (Divide by 2)
# ✔ Binary Basics are essential for Bit Manipulation.
# ✔ Very Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# BIT MANIPULATION - Batch 1 COMPLETE ✅
# ============================================================

# ============================================================
# BIT MANIPULATION PATTERN - Batch 2
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 4. SINGLE NUMBER
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me array ke sabhi elements do baar aate hain, sirf ek element
ek hi baar hota hai. XOR (^) operator ki property hoti hai ki same
numbers ka XOR 0 hota hai aur 0 ka kisi number ke saath XOR wahi number
hota hai. Isliye poori array ka XOR karne par duplicate numbers cancel
ho jate hain aur sirf unique number bach jata hai. Ye TCS Prime aur
service-based interviews ka bahut common Bit Manipulation question hai.
"""

def single_number(arr):

    answer = 0

    for num in arr:

        answer ^= num

    return answer


arr = [2,2,1]

print("Single Number :")
print(single_number(arr))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 5. MISSING NUMBER (Using XOR)
# ============================================================

"""
THEORY (Interview Explanation)

Array me numbers 0 se n tak hote hain aur ek number missing hota hai.
XOR ki property ka use karke hum 0 se n tak ke sabhi numbers aur array
ke sabhi elements ka XOR kar dete hain. Same numbers cancel ho jate hain
aur last me sirf missing number bachta hai. Is approach me extra memory
ki zarurat nahi hoti aur ye O(n) time me solution deta hai.
"""

def missing_number(arr):

    n = len(arr)

    answer = 0

    for i in range(n + 1):

        answer ^= i

    for num in arr:

        answer ^= num

    return answer


arr = [3,0,1]

print()

print("Missing Number :")
print(missing_number(arr))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 6. SWAP TWO NUMBERS (Using XOR)
# ============================================================

"""
THEORY (Interview Explanation)

Do variables ko third variable ke bina swap karne ke liye XOR operator
ka use kiya ja sakta hai. Pehle a = a ^ b, fir b = a ^ b aur last me
a = a ^ b karte hain. XOR ki properties ki wajah se dono values exchange
ho jati hain. Interview me ye concept Bit Manipulation samajhne ke liye
pucha jata hai, lekin practical Python code me normal swapping
(a, b = b, a) ko hi prefer kiya jata hai.
"""

def swap_numbers(a, b):

    a ^= b

    b ^= a

    a ^= b

    return a, b


print()

print("Swap Numbers :")
print(swap_numbers(10, 20))


# ============================================================
# Expected Output
# ============================================================

# Single Number :
# 1

# Missing Number :
# 2

# Swap Numbers :
# (20, 10)


# ============================================================
# Complexity
# ============================================================

# Single Number
# Time  : O(n)
# Space : O(1)

# Missing Number (XOR)
# Time  : O(n)
# Space : O(1)

# Swap Two Numbers
# Time  : O(1)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ a ^ a = 0
# ✔ a ^ 0 = a
# ✔ XOR removes duplicate values.
# ✔ XOR can find missing or unique numbers.
# ✔ Python prefers (a, b = b, a) in real projects,
#   but XOR swapping is a common interview concept.

# ============================================================
# BIT MANIPULATION - Batch 2 COMPLETE ✅
# ============================================================

# ============================================================
# BIT MANIPULATION PATTERN - Batch 3
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 7. FIND i-th BIT
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me hume kisi number ka i-th bit check karna hota hai.
Iske liye number ko i positions right shift karte hain aur last bit
check karte hain. Dusra tarika (1 << i) mask banana hai. Dono methods
interview me acceptable hain. Ye concept Bit Manipulation ki foundation
hai aur isi se Set Bit, Clear Bit aur Toggle Bit wale questions bante
hain.
"""

def find_ith_bit(n, i):

    return (n >> i) & 1


print("Find i-th Bit :")
print(find_ith_bit(13, 2))

# 13 = 1101
# Bit at index 2 = 1

# Time  : O(1)
# Space : O(1)



# ============================================================
# 8. SET i-th BIT
# ============================================================

"""
THEORY (Interview Explanation)

Set Bit ka matlab kisi specific bit ko 1 banana hota hai.
Agar bit pehle se 1 hai to value same rehti hai.
Agar 0 hai to 1 ban jati hai. Iske liye OR (|) operator
aur (1 << i) mask use kiya jata hai. OR operation sirf
required bit ko set karta hai, baaki bits unchanged rehti hain.
"""

def set_ith_bit(n, i):

    return n | (1 << i)


print()

print("Set i-th Bit :")
print(set_ith_bit(9, 1))

# 9 = 1001
# Output = 1011 = 11

# Time  : O(1)
# Space : O(1)



# ============================================================
# 9. CLEAR i-th BIT
# ============================================================

"""
THEORY (Interview Explanation)

Clear Bit ka matlab kisi specific bit ko 0 banana hota hai.
Iske liye pehle (1 << i) mask banate hain, fir NOT (~)
laga kar us bit ko 0 aur baaki sab bits ko 1 bana dete hain.
Uske baad AND (&) operation karte hain. Sirf target bit clear
hoti hai aur baaki bits same rehti hain.
"""

def clear_ith_bit(n, i):

    return n & ~(1 << i)


print()

print("Clear i-th Bit :")
print(clear_ith_bit(13, 2))

# 13 = 1101
# Output = 1001 = 9

# Time  : O(1)
# Space : O(1)



# ============================================================
# 10. TOGGLE i-th BIT
# ============================================================

"""
THEORY (Interview Explanation)

Toggle Bit ka matlab 0 ko 1 aur 1 ko 0 banana hota hai.
Iske liye XOR (^) operator use karte hain.
Agar bit 1 hai to XOR usse 0 bana dega aur agar bit 0 hai
to XOR usse 1 bana dega. Toggle operation switching logic,
flags aur state management me kaafi use hota hai.
"""

def toggle_ith_bit(n, i):

    return n ^ (1 << i)


print()

print("Toggle i-th Bit :")
print(toggle_ith_bit(13, 2))

# 13 = 1101
# Output = 1001 = 9

# Time  : O(1)
# Space : O(1)



# ============================================================
# 11. FIND ODD OCCURRING NUMBER
# ============================================================

"""
THEORY (Interview Explanation)

Array me sabhi elements even number of times aate hain aur
sirf ek element odd number of times aata hai. XOR ki property
(a ^ a = 0) ki wajah se sabhi duplicate elements cancel ho
jate hain aur sirf odd occurring element bach jata hai.
Ye Single Number ka hi extension hai aur service-based
companies me frequently pucha jata hai.
"""

def odd_occurring(arr):

    answer = 0

    for num in arr:

        answer ^= num

    return answer


arr = [4,3,4,4,4,5,5]

print()

print("Odd Occurring Number :")
print(odd_occurring(arr))


# ============================================================
# Expected Output
# ============================================================

# Find i-th Bit :
# 1

# Set i-th Bit :
# 11

# Clear i-th Bit :
# 9

# Toggle i-th Bit :
# 9

# Odd Occurring Number :
# 3


# ============================================================
# Complexity
# ============================================================

# Find i-th Bit          O(1)
# Set i-th Bit           O(1)
# Clear i-th Bit         O(1)
# Toggle i-th Bit        O(1)
# Odd Occurring Number   O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Find Bit   -> (n >> i) & 1
# ✔ Set Bit    -> n | (1 << i)
# ✔ Clear Bit  -> n & ~(1 << i)
# ✔ Toggle Bit -> n ^ (1 << i)
# ✔ XOR removes duplicate values.
# ✔ Very Frequently Asked in TCS Prime.

# ============================================================
# BIT MANIPULATION PATTERN COMPLETE ✅
# ============================================================