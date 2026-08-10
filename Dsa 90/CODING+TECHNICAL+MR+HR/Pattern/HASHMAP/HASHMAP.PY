# ============================================================
# HASHMAP / DICTIONARY PATTERN - Batch 1 (Frequency Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. FREQUENCY OF ELEMENTS
# ============================================================

"""
THEORY (Interview Explanation)

Frequency of Elements HashMap ka sabse basic aur important question hai.
HashMap (Dictionary) key-value pair store karta hai jahan key element
hota hai aur value uski frequency hoti hai. Har element ko traverse
karke uska count update karte hain. Isi concept se Duplicate, Majority,
Top Frequency aur Count Distinct jaise bahut saare interview questions
bante hain. Ye TCS Prime aur service-based companies ka foundation
question hai.
"""

def frequency_of_elements(arr):

    frequency = {}

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

    return frequency


arr = [1,2,2,3,1,4,2]

print("Frequency of Elements :")
print(frequency_of_elements(arr))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. WORD FREQUENCY
# ============================================================

"""
THEORY (Interview Explanation)

Word Frequency me sentence ke har word ka count nikalna hota hai.
Sentence ko split() se words me convert karte hain aur HashMap me
har word ki frequency store karte hain. Ye text processing, search
engines aur NLP applications ka basic concept hai. Interview me ye
Character Frequency ka extension mana jata hai.
"""

def word_frequency(sentence):

    frequency = {}

    for word in sentence.split():

        frequency[word] = frequency.get(word, 0) + 1

    return frequency


print()

print("Word Frequency :")
print(word_frequency("python java python c java python"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. MAXIMUM FREQUENCY ELEMENT
# ============================================================

"""
THEORY (Interview Explanation)

Maximum Frequency Element me array ka sabse jyada baar aane wala
element find karna hota hai. Pehle frequency map banate hain aur
phir us dictionary ko traverse karke maximum frequency aur uska
element track karte hain. Ye Majority aur Top-K problems ka base
concept hai.
"""

def maximum_frequency_element(arr):

    frequency = {}

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

    answer = None

    maximum = 0

    for key, value in frequency.items():

        if value > maximum:

            maximum = value

            answer = key

    return answer


print()

print("Maximum Frequency Element :")
print(maximum_frequency_element(arr))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. COUNT DISTINCT ELEMENTS
# ============================================================

"""
THEORY (Interview Explanation)

Distinct Elements ka matlab unique values hoti hain, frequency nahi.
HashMap ya Set dono use kiye ja sakte hain. Set automatically duplicate
values ko remove kar deta hai, isliye uski length distinct elements ki
count hoti hai. Ye interview me bahut common aur easy question hai.
"""

def count_distinct_elements(arr):

    return len(set(arr))


print()

print("Count Distinct Elements :")
print(count_distinct_elements(arr))


# ============================================================
# Expected Output
# ============================================================

# Frequency of Elements :
# {1:2, 2:3, 3:1, 4:1}

# Word Frequency :
# {'python':3, 'java':2, 'c':1}

# Maximum Frequency Element :
# 2

# Count Distinct Elements :
# 4


# ============================================================
# Complexity
# ============================================================

# Frequency of Elements
# Time  : O(n)
# Space : O(n)

# Word Frequency
# Time  : O(n)
# Space : O(n)

# Maximum Frequency Element
# Time  : O(n)
# Space : O(n)

# Count Distinct Elements
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Dictionary stores (Key → Frequency).
# ✔ get(key, 0) avoids KeyError.
# ✔ Set automatically removes duplicates.
# ✔ Frequency Pattern is the base of most HashMap problems.
# ✔ One of the highest-frequency patterns in TCS Prime.

# ============================================================
# HASHMAP - Batch 1 COMPLETE ✅
# ============================================================

# ============================================================
# HASHMAP / DICTIONARY PATTERN - Batch 2
# (Duplicate + Unique Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. FIND DUPLICATE ELEMENTS
# ============================================================

"""
THEORY (Interview Explanation)

Duplicate Elements ka matlab wo values jo array me ek se zyada baar
aati hain. Sabse pehle HashMap me har element ki frequency store karte
hain. Uske baad jis element ki frequency 1 se zyada hoti hai, wo
duplicate hota hai. Ye HashMap Pattern ka basic interview question hai
aur isi concept se Duplicate Count aur Remove Duplicates jaise problems
banti hain.
"""

def find_duplicates(arr):

    frequency = {}

    result = []

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

    for key, value in frequency.items():

        if value > 1:

            result.append(key)

    return result


arr = [1,2,3,2,4,5,1,6,2]

print("Find Duplicate Elements :")
print(find_duplicates(arr))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. PRINT DUPLICATE ELEMENTS
# ============================================================

"""
THEORY (Interview Explanation)

Print Duplicate Elements aur Find Duplicate Elements ka logic same hota
hai. Difference sirf output format ka hota hai. Frequency map banane ke
baad sirf un elements ko print karte hain jinki frequency 1 se zyada
ho. Interview me ye direct HashMap implementation test karta hai.
"""

def print_duplicates(arr):

    frequency = {}

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

    for key, value in frequency.items():

        if value > 1:

            print(key, end=" ")


print()

print("Print Duplicate Elements :")
print_duplicates(arr)


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. CHECK DUPLICATE EXISTS
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me sirf check karna hota hai ki array me koi duplicate
element present hai ya nahi. HashSet sabse efficient approach hai.
Har element ko set me add karte hain. Agar koi element pehle se set me
mil jaye to duplicate exist karta hai aur True return kar dete hain.
Ye O(n) solution hai.
"""

def duplicate_exists(arr):

    visited = set()

    for num in arr:

        if num in visited:

            return True

        visited.add(num)

    return False


print()

print("Duplicate Exists :")
print(duplicate_exists(arr))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. UNIQUE ELEMENTS
# ============================================================

"""
THEORY (Interview Explanation)

Unique Elements wo hote hain jo array me sirf ek baar aaye hon.
Frequency map banane ke baad frequency == 1 wale elements ko answer
list me add karte hain. Ye Duplicate Pattern ka reverse concept hai
aur interview me frequently pucha jata hai.
"""

def unique_elements(arr):

    frequency = {}

    result = []

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

    for key, value in frequency.items():

        if value == 1:

            result.append(key)

    return result


print()

print("Unique Elements :")
print(unique_elements(arr))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 5. FIRST UNIQUE ELEMENT
# ============================================================

"""
THEORY (Interview Explanation)

First Unique Element ka matlab array ka pehla aisa element jiska
frequency sirf 1 ho. Pehle frequency map banate hain, phir original
array ko dobara traverse karte hain. Pehla frequency 1 wala element
milte hi return kar dete hain. Agar koi unique element nahi ho to -1
return karte hain.
"""

def first_unique_element(arr):

    frequency = {}

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

    for num in arr:

        if frequency[num] == 1:

            return num

    return -1


print()

print("First Unique Element :")
print(first_unique_element(arr))


# ============================================================
# Expected Output
# ============================================================

# Find Duplicate Elements :
# [1, 2]

# Print Duplicate Elements :
# 1 2

# Duplicate Exists :
# True

# Unique Elements :
# [3, 4, 5, 6]

# First Unique Element :
# 3


# ============================================================
# Complexity
# ============================================================

# Find Duplicate Elements
# Time  : O(n)
# Space : O(n)

# Print Duplicate Elements
# Time  : O(n)
# Space : O(n)

# Duplicate Exists
# Time  : O(n)
# Space : O(n)

# Unique Elements
# Time  : O(n)
# Space : O(n)

# First Unique Element
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Dictionary stores frequencies.
# ✔ Set is best for duplicate checking.
# ✔ Frequency > 1 → Duplicate
# ✔ Frequency == 1 → Unique
# ✔ Very Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# HASHMAP - Batch 2 COMPLETE ✅
# ============================================================


# ============================================================
# HASHMAP / DICTIONARY PATTERN - Batch 3
# (Occurrence + Majority Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. FIRST REPEATING ELEMENT
# ============================================================

"""
THEORY (Interview Explanation)

First Repeating Element ka matlab array ka pehla aisa element jo dobara
appear hota hai. HashSet is problem ka sabse efficient solution hai.
Array ko left se right traverse karte hain. Agar current element pehle
se HashSet me present hai to wahi first repeating element hota hai.
Agar traversal complete ho jaye aur duplicate na mile to -1 return
karte hain. Ye HashMap/HashSet Pattern ka bahut common interview
question hai.
"""

def first_repeating_element(arr):

    visited = set()

    for num in arr:

        if num in visited:

            return num

        visited.add(num)

    return -1


arr = [10,5,3,4,3,5,6]

print("First Repeating Element :")
print(first_repeating_element(arr))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. FIRST NON-REPEATING ELEMENT
# ============================================================

"""
THEORY (Interview Explanation)

First Non-Repeating Element ka matlab array ka pehla aisa element
jiski frequency sirf ek ho. Pehle HashMap me sabhi elements ki
frequency store karte hain. Fir original array ko dobara traverse
karte hain aur pehla frequency 1 wala element return kar dete hain.
Ye Frequency Pattern ka standard application hai.
"""

def first_non_repeating_element(arr):

    frequency = {}

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

    for num in arr:

        if frequency[num] == 1:

            return num

    return -1


print()

print("First Non-Repeating Element :")
print(first_non_repeating_element(arr))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. MAJORITY ELEMENT (> n/2)
# ============================================================

"""
THEORY (Interview Explanation)

Majority Element wo hota hai jo array me n/2 se zyada baar appear ho.
Service-based companies me HashMap solution generally accepted hota hai.
Pehle frequency map banate hain aur fir check karte hain ki kis element
ki frequency array size ke half se zyada hai. Agar koi majority element
na ho to -1 return karte hain. Product companies Boyer-Moore Algorithm
bhi puch sakti hain, lekin TCS Prime me HashMap approach sufficient hai.
"""

def majority_element(arr):

    frequency = {}

    limit = len(arr) // 2

    for num in arr:

        frequency[num] = frequency.get(num, 0) + 1

        if frequency[num] > limit:

            return num

    return -1


arr2 = [2,2,1,2,3,2,2]

print()

print("Majority Element :")
print(majority_element(arr2))


# ============================================================
# Expected Output
# ============================================================

# First Repeating Element :
# 3

# First Non-Repeating Element :
# 10

# Majority Element :
# 2


# ============================================================
# Complexity
# ============================================================

# First Repeating Element
# Time  : O(n)
# Space : O(n)

# First Non-Repeating Element
# Time  : O(n)
# Space : O(n)

# Majority Element
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ HashSet is best for detecting repetition.
# ✔ HashMap stores frequencies.
# ✔ Frequency == 1 → Non-Repeating.
# ✔ Frequency > n//2 → Majority Element.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.


# ============================================================
# HASHMAP - Batch 3 COMPLETE ✅
# ============================================================


# ============================================================
# HASHMAP / DICTIONARY PATTERN - Batch 4
# (Pair Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. TWO SUM
# ============================================================

"""
THEORY (Interview Explanation)

Two Sum HashMap Pattern ka sabse famous interview question hai. Hume
array me do aise elements find karne hote hain jinka sum target ke
equal ho. Brute Force O(n²) hota hai, lekin HashMap se O(n) me solve
kar sakte hain. Har element ke liye target - current element
(complement) calculate karte hain. Agar complement HashMap me already
present hai to answer mil gaya, warna current element ko HashMap me
store kar dete hain. Ye TCS Prime ka highest-frequency HashMap problem
hai.
"""

def two_sum(arr, target):

    hashmap = {}

    for i in range(len(arr)):

        complement = target - arr[i]

        if complement in hashmap:

            return [hashmap[complement], i]

        hashmap[arr[i]] = i

    return []


arr = [2, 7, 11, 15]

print("Two Sum :")
print(two_sum(arr, 9))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. COUNT PAIRS WITH GIVEN SUM
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me target sum banane wale total pairs count karne hote hain.
HashMap me frequency maintain karte hain. Har naye element ke liye
target - current element check karte hain. Agar complement pehle se
HashMap me hai to uski frequency jitne valid pairs add kar dete hain.
Uske baad current element ki frequency update karte hain. Ye Two Sum ka
extension hai aur service-based interviews me kaafi common hai.
"""

def count_pairs_with_sum(arr, target):

    hashmap = {}

    count = 0

    for num in arr:

        complement = target - num

        if complement in hashmap:

            count += hashmap[complement]

        hashmap[num] = hashmap.get(num, 0) + 1

    return count


arr = [1, 5, 7, -1, 5]

print()

print("Count Pairs With Given Sum :")
print(count_pairs_with_sum(arr, 6))


# ============================================================
# Expected Output
# ============================================================

# Two Sum :
# [0, 1]

# Count Pairs With Given Sum :
# 3


# ============================================================
# Complexity
# ============================================================

# Two Sum
# Time  : O(n)
# Space : O(n)

# Count Pairs With Given Sum
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Complement = Target - Current Element
# ✔ HashMap stores value → index (Two Sum)
# ✔ HashMap stores value → frequency (Pair Count)
# ✔ Brute Force = O(n²)
# ✔ Optimized HashMap = O(n)
# ✔ One of the most frequently asked HashMap problems in
#   TCS Prime & Service-Based Companies.

# ============================================================
# HASHMAP - Batch 4 COMPLETE ✅
# ============================================================


# ============================================================
# HASHMAP / DICTIONARY PATTERN - Batch 5
# (Subarray Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. SUBARRAY SUM = K
# ============================================================

"""
THEORY (Interview Explanation)

Subarray Sum = K me check karna hota hai ki koi continuous subarray
target sum K ke equal hai ya nahi. Prefix Sum aur HashMap ka use karke
O(n) solution milta hai. Har step par current prefix sum nikalte hain.
Agar (current_sum - K) pehle HashMap me present hai to beech ka subarray
K ke equal hoga. Ye TCS Prime ka bahut important Prefix + HashMap
question hai.
"""

def subarray_sum_k(arr, k):

    prefix = {0: -1}

    current_sum = 0

    for i in range(len(arr)):

        current_sum += arr[i]

        if current_sum - k in prefix:

            return True

        prefix[current_sum] = i

    return False


arr = [1,2,3,7,5]

print("Subarray Sum = K :")
print(subarray_sum_k(arr, 12))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. COUNT SUBARRAYS WITH SUM = K
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me target sum K wale total subarrays count karne hote hain.
HashMap me prefix sum ki frequency store karte hain. Agar
(current_sum - K) pehle aa chuka hai to uski frequency jitne valid
subarrays mil jayenge. Ye Prefix Sum Pattern ka sabse famous interview
question hai.
"""

def count_subarrays_sum_k(arr, k):

    prefix = {0: 1}

    current_sum = 0

    count = 0

    for num in arr:

        current_sum += num

        count += prefix.get(current_sum - k, 0)

        prefix[current_sum] = prefix.get(current_sum, 0) + 1

    return count


arr = [1,1,1]

print()

print("Count Subarrays With Sum = K :")
print(count_subarrays_sum_k(arr, 2))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. LONGEST SUBARRAY WITH SUM = K
# ============================================================

"""
THEORY (Interview Explanation)

Longest Subarray Sum = K me maximum length ka subarray find karna hota
hai. Prefix Sum ka first occurrence HashMap me store karte hain.
Agar (current_sum - K) mil jaye to current index aur uske first
occurrence ka difference longest length update kar deta hai. Ye TCS
Prime aur Infosys me frequently pucha jata hai.
"""

def longest_subarray_sum_k(arr, k):

    prefix = {}

    current_sum = 0

    maximum = 0

    for i in range(len(arr)):

        current_sum += arr[i]

        if current_sum == k:

            maximum = i + 1

        if current_sum not in prefix:

            prefix[current_sum] = i

        if current_sum - k in prefix:

            maximum = max(maximum, i - prefix[current_sum - k])

    return maximum


arr = [10,5,2,7,1,9]

print()

print("Longest Subarray Sum = K :")
print(longest_subarray_sum_k(arr, 15))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. ZERO SUM SUBARRAY
# ============================================================

"""
THEORY (Interview Explanation)

Zero Sum Subarray me check karna hota hai ki kisi continuous subarray
ka sum zero hai ya nahi. Agar same prefix sum dobara mil jaye to beech
ka subarray zero sum hoga. Isi wajah se Prefix Sum ko HashSet me store
karna sufficient hai. Ye service-based interviews ka common question
hai.
"""

def zero_sum_subarray(arr):

    prefix = set()

    current_sum = 0

    for num in arr:

        current_sum += num

        if current_sum == 0 or current_sum in prefix:

            return True

        prefix.add(current_sum)

    return False


arr = [4,2,-3,1,6]

print()

print("Zero Sum Subarray :")
print(zero_sum_subarray(arr))


# ============================================================
# Expected Output
# ============================================================

# Subarray Sum = K :
# True

# Count Subarrays With Sum = K :
# 2

# Longest Subarray Sum = K :
# 4

# Zero Sum Subarray :
# True


# ============================================================
# Complexity
# ============================================================

# Subarray Sum = K
# Time  : O(n)
# Space : O(n)

# Count Subarrays With Sum = K
# Time  : O(n)
# Space : O(n)

# Longest Subarray Sum = K
# Time  : O(n)
# Space : O(n)

# Zero Sum Subarray
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Prefix Sum + HashMap = O(n)
# ✔ current_sum - K is the key concept.
# ✔ Store first occurrence for longest subarray.
# ✔ Repeated Prefix Sum ⇒ Zero Sum Subarray.
# ✔ Highest-frequency HashMap pattern in TCS Prime.

# ============================================================
# HASHMAP - Batch 5 COMPLETE ✅
# ============================================================


# ============================================================
# HASHMAP / DICTIONARY PATTERN - Batch 6
# (Prefix + Set Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. CONTINUOUS SUBARRAY SUM
# ============================================================

"""
THEORY (Interview Explanation)

Is problem me check karna hota hai ki koi continuous subarray exist
karta hai ya nahi jiska sum k ka multiple ho. Prefix Sum aur remainder
(HashMap) ka use kiya jata hai. Agar same remainder dobara mil jaye aur
distance kam se kam 2 ho to beech ka subarray k ka multiple hoga. Ye
Prefix Sum + HashMap ka standard interview question hai.
"""

def continuous_subarray_sum(nums, k):

    remainder_map = {0: -1}

    prefix_sum = 0

    for i in range(len(nums)):

        prefix_sum += nums[i]

        remainder = prefix_sum % k if k != 0 else prefix_sum

        if remainder in remainder_map:

            if i - remainder_map[remainder] >= 2:

                return True

        else:

            remainder_map[remainder] = i

    return False


nums = [23,2,4,6,7]

print("Continuous Subarray Sum :")
print(continuous_subarray_sum(nums, 6))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. LONGEST CONSECUTIVE SEQUENCE
# ============================================================

"""
THEORY (Interview Explanation)

Longest Consecutive Sequence me longest consecutive numbers ki length
find karni hoti hai. Sabhi numbers ko HashSet me store karte hain.
Sirf wahi numbers sequence start karte hain jinke pehle wala number
set me nahi hota. Fir next consecutive numbers count karte hain.
Ye O(n) optimized solution hai aur service-based interviews me
frequently pucha jata hai.
"""

def longest_consecutive(nums):

    numbers = set(nums)

    longest = 0

    for num in numbers:

        if num - 1 not in numbers:

            length = 1

            while num + length in numbers:

                length += 1

            longest = max(longest, length)

    return longest


nums = [100,4,200,1,3,2]

print()

print("Longest Consecutive Sequence :")
print(longest_consecutive(nums))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. MISSING NUMBER
# ============================================================

"""
THEORY (Interview Explanation)

Array me 0 se n tak ke numbers hote hain aur ek number missing hota
hai. HashSet me sabhi elements store karke 0 se n tak iterate karte
hain. Jo number set me nahi milta wahi missing number hota hai.
Ye basic HashSet implementation question hai.
"""

def missing_number(nums):

    numbers = set(nums)

    for i in range(len(nums) + 1):

        if i not in numbers:

            return i


nums = [3,0,1]

print()

print("Missing Number :")
print(missing_number(nums))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 4. INTERSECTION OF ARRAYS
# ============================================================

"""
THEORY (Interview Explanation)

Intersection ka matlab common elements. Ek array ko HashSet me store
karte hain aur doosre array ko traverse karte hain. Jo elements set me
milte hain unhe result me add kar dete hain. Result ko set me rakhne se
duplicate values automatically remove ho jati hain.
"""

def intersection(nums1, nums2):

    set1 = set(nums1)

    result = set()

    for num in nums2:

        if num in set1:

            result.add(num)

    return list(result)


print()

print("Intersection :")
print(intersection([1,2,2,1],[2,2]))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 5. UNION OF ARRAYS
# ============================================================

"""
THEORY (Interview Explanation)

Union ka matlab dono arrays ke sabhi unique elements. HashSet use
karne se duplicate values automatically remove ho jati hain. Dono
arrays ko set me add karke final unique elements return kar dete hain.
Ye HashSet ka sabse basic application hai.
"""

def union(nums1, nums2):

    return list(set(nums1) | set(nums2))


print()

print("Union :")
print(union([1,2,3],[3,4,5]))


# ============================================================
# Expected Output
# ============================================================

# Continuous Subarray Sum :
# True

# Longest Consecutive Sequence :
# 4

# Missing Number :
# 2

# Intersection :
# [2]

# Union :
# [1,2,3,4,5]


# ============================================================
# Complexity
# ============================================================

# Continuous Subarray Sum
# Time  : O(n)
# Space : O(n)

# Longest Consecutive Sequence
# Time  : O(n)
# Space : O(n)

# Missing Number
# Time  : O(n)
# Space : O(n)

# Intersection
# Time  : O(n)
# Space : O(n)

# Union
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Prefix Sum + Remainder → Continuous Subarray Sum
# ✔ HashSet → Fast Lookup (O(1))
# ✔ Consecutive Sequence starts only when (num-1) is absent.
# ✔ Intersection = Common Elements
# ✔ Union = All Unique Elements
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# HASHMAP - Batch 6 COMPLETE ✅
# ============================================================


# ============================================================
# HASHMAP / DICTIONARY PATTERN - Batch 7
# (Interview Mixed Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. ISOMORPHIC STRINGS
# ============================================================

"""
THEORY (Interview Explanation)

Do strings Isomorphic tab hoti hain jab first string ka har character
second string ke sirf ek unique character se map ho aur mapping
consistent rahe. Ek character do alag characters se map nahi ho sakta.
Iske liye do HashMaps maintain karte hain, ek s→t aur ek t→s. Har
character pair ko verify karte hain. Ye HashMap ka standard interview
question hai aur TCS Prime me pucha ja sakta hai.
"""

def is_isomorphic(s, t):

    if len(s) != len(t):

        return False

    map1 = {}
    map2 = {}

    for i in range(len(s)):

        if s[i] in map1 and map1[s[i]] != t[i]:

            return False

        if t[i] in map2 and map2[t[i]] != s[i]:

            return False

        map1[s[i]] = t[i]
        map2[t[i]] = s[i]

    return True


print("Isomorphic Strings :")
print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 2. RANSOM NOTE
# ============================================================

"""
THEORY (Interview Explanation)

Ransom Note problem me check karna hota hai ki magazine ke characters
use karke ransom note ban sakta hai ya nahi. Magazine ke characters ki
frequency HashMap me store karte hain. Fir ransom note ke har character
ko consume karte hain. Agar kisi character ki frequency zero ho jaye
to note banana possible nahi hai.
"""

def ransom_note(note, magazine):

    frequency = {}

    for ch in magazine:

        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in note:

        if frequency.get(ch, 0) == 0:

            return False

        frequency[ch] -= 1

    return True


print()

print("Ransom Note :")
print(ransom_note("aa", "aab"))
print(ransom_note("aa", "ab"))


# Time  : O(n)
# Space : O(n)



# ============================================================
# 3. JEWELS AND STONES
# ============================================================

"""
THEORY (Interview Explanation)

Jewels and Stones me ek string jewels hoti hai aur doosri stones.
Count karna hota hai ki stones me kitne characters jewels me present
hain. Jewels ko HashSet me store karte hain jisse lookup O(1) ho jata
hai. Fir stones traverse karke count increase karte hain. Ye HashSet
ka simple aur common interview question hai.
"""

def jewels_and_stones(jewels, stones):

    jewel_set = set(jewels)

    count = 0

    for ch in stones:

        if ch in jewel_set:

            count += 1

    return count


print()

print("Jewels and Stones :")
print(jewels_and_stones("aA", "aAAbbbb"))


# ============================================================
# Expected Output
# ============================================================

# Isomorphic Strings :
# True
# False

# Ransom Note :
# True
# False

# Jewels and Stones :
# 3


# ============================================================
# Complexity
# ============================================================

# Isomorphic Strings
# Time  : O(n)
# Space : O(n)

# Ransom Note
# Time  : O(n)
# Space : O(n)

# Jewels and Stones
# Time  : O(n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Two-way HashMap → Isomorphic Strings
# ✔ Frequency HashMap → Ransom Note
# ✔ HashSet → Fast Membership Checking
# ✔ Average HashMap Lookup = O(1)
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.


# ============================================================
# HASHMAP PATTERN COMPLETE ✅
# ============================================================

