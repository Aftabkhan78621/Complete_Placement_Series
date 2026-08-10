# ============================================================
# SORTING PATTERN - 1
# BUBBLE SORT
# ============================================================

"""
THEORY (Interview Explanation)

Bubble Sort ek simple comparison-based sorting algorithm hai jisme hum
adjacent (paas-paas) elements ko compare karte hain. Agar left element
right element se bada hota hai to dono ko swap kar dete hain. Har pass
ke baad sabse bada element automatically array ke end me pahunch jata
hai, isi wajah se ise Bubble Sort kehte hain. Agar array pehle se sorted
ho to swapped flag ki madad se algorithm jaldi terminate ho jata hai.
Ye stable aur in-place sorting algorithm hai. Service-based companies
isme mainly logic, swapping aur nested loops ka concept check karti hain.
"""

def bubble_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        swapped = False

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:
            break

    return arr


arr = [5, 3, 8, 4, 2]

print("Bubble Sort :", bubble_sort(arr))


# Complexity
# Best    : O(n)
# Average : O(n²)
# Worst   : O(n²)
# Space   : O(1)

# Stable  : Yes
# In-place: Yes


# ============================================================
# SORTING PATTERN - 2
# SELECTION SORT
# ============================================================

"""
THEORY (Interview Explanation)

Selection Sort me har pass me unsorted part ka sabse chhota element
find kiya jata hai aur use current position par swap kar diya jata hai.
Pehle pass me smallest element first position par, dusre pass me second
smallest second position par aa jata hai. Is algorithm me comparisons
hamesha same rehte hain, chahe array sorted ho ya nahi. Ye in-place
sorting algorithm hai lekin stable nahi hai. Bubble Sort ki tarah isme
baar-baar swapping nahi hoti, isliye swaps kam hote hain, lekin overall
time complexity fir bhi O(n²) hi rehti hai.
"""

def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        minimum = i

        for j in range(i + 1, n):

            if arr[j] < arr[minimum]:

                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr


arr = [5, 3, 8, 4, 2]

print("Selection Sort :", selection_sort(arr))


# Complexity
# Best    : O(n²)
# Average : O(n²)
# Worst   : O(n²)
# Space   : O(1)

# Stable  : No
# In-place: Yes



# ============================================================
# SORTING PATTERN - 3
# INSERTION SORT
# ============================================================

"""
THEORY (Interview Explanation)

Insertion Sort cards arrange karne jaisa algorithm hai. Hum array ke
second element se start karte hain aur current element ko uski correct
position par insert karte hain. Left side hamesha sorted maintain hoti
hai aur right side unsorted rehti hai. Agar array already sorted ho to
ye bahut fast kaam karta hai aur O(n) time leta hai. Isliye small arrays
aur nearly sorted arrays ke liye ye Bubble aur Selection Sort se better
mana jata hai. Ye stable aur in-place sorting algorithm hai.
"""

def insertion_sort(arr):

    n = len(arr)

    for i in range(1, n):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


arr = [5, 3, 8, 4, 2]

print("Insertion Sort :", insertion_sort(arr))


# Complexity
# Best    : O(n)
# Average : O(n²)
# Worst   : O(n²)
# Space   : O(1)

# Stable  : Yes
# In-place: Yes

# ============================================================
# SORTING PATTERN - 4
# MERGE SORT
# ============================================================

"""
THEORY (Interview Explanation)

Merge Sort ek Divide and Conquer algorithm hai. Isme array ko repeatedly
2 equal parts me divide kiya jata hai jab tak har part me sirf ek
element na bach jaye. Phir un parts ko compare karke sorted order me
merge kiya jata hai. Kyunki har level par merging O(n) hoti hai aur
total log n levels hote hain, iski time complexity O(n log n) hoti hai.
Ye large datasets ke liye bahut efficient hai. Merge Sort stable sorting
algorithm hai lekin extra memory use karta hai, isliye ye in-place nahi
hai.
"""

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])

    right = merge_sort(arr[mid:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [5,3,8,4,2]

print("Merge Sort :", merge_sort(arr))


# Complexity
# Best    : O(n log n)
# Average : O(n log n)
# Worst   : O(n log n)
# Space   : O(n)

# Stable  : Yes
# In-place: No

# ============================================================
# SORTING PATTERN - 5
# QUICK SORT
# ============================================================

"""
THEORY (Interview Explanation)

Quick Sort bhi Divide and Conquer algorithm hai. Isme ek pivot element
select kiya jata hai aur array ko is tarah partition kiya jata hai ki
pivot se chhote elements left side aur bade elements right side aa
jaate hain. Fir dono parts par recursively same process repeat hota hai.
Average case me ye bahut fast hota hai aur O(n log n) time leta hai,
isliye real-world applications me kaafi use hota hai. Lekin agar pivot
baar-baar galat choose ho jaye to worst case O(n²) ho sakta hai. Ye
generally in-place hai lekin stable nahi hai.
"""

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]

    middle = [x for x in arr if x == pivot]

    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [5,3,8,4,2]

print("Quick Sort :", quick_sort(arr))


# Complexity
# Best    : O(n log n)
# Average : O(n log n)
# Worst   : O(n²)
# Space   : O(log n) recursion stack
# (This implementation uses extra lists.)

# Stable  : No
# In-place: Generally Yes (classic partition version)

# ============================================================
# SORTING PATTERN - 6
# MERGE INTERVALS
# ============================================================

"""
THEORY (Interview Explanation)

Merge Intervals ek important sorting problem hai. Sabse pehle intervals
ko unke starting point ke basis par sort kiya jata hai. Uske baad ek-ek
interval ko previous interval se compare kiya jata hai. Agar dono
overlap karte hain to unhe merge kar diya jata hai, warna naye interval
ko result me add kar diya jata hai. Ye problem meetings, bookings,
calendar scheduling aur time-slot merging jaise real-world scenarios me
kaafi use hoti hai. Interview me Sorting + Greedy concept check karne ke
liye frequently puchi jati hai.
"""

def merge_intervals(intervals):

    intervals.sort()

    result = [intervals[0]]

    for start, end in intervals[1:]:

        last_end = result[-1][1]

        if start <= last_end:

            result[-1][1] = max(last_end, end)

        else:

            result.append([start, end])

    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]

print("Merge Intervals :", merge_intervals(intervals))


# Complexity
# Time  : O(n log n)
# Space : O(n)

# Stable  : Depends on sorting implementation
# In-place: No

# ============================================================
# SORTING PATTERN - 7
# RELATIVE SORT ARRAY
# ============================================================

"""
THEORY (Interview Explanation)

Relative Sort Array me ek array ko doosre array ke order ke according
sort karna hota hai. Jo elements second array me hote hain unhe usi
sequence me rakha jata hai, aur jo elements nahi hote unhe ascending
order me last me add kiya jata hai. Is problem me HashMap aur Sorting
dono ka combination use hota hai. Ye service-based companies me
occasionally pucha jata hai aur frequency counting ka concept bhi test
karta hai.
"""

from collections import Counter

def relative_sort(arr1, arr2):

    frequency = Counter(arr1)

    result = []

    for num in arr2:

        result.extend([num] * frequency[num])

        frequency.pop(num, None)

    remaining = []

    for num, count in frequency.items():

        remaining.extend([num] * count)

    result.extend(sorted(remaining))

    return result


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print("Relative Sort :", relative_sort(arr1, arr2))


# Complexity
# Time  : O(n log n)
# Space : O(n)

# ============================================================
# SORTING PATTERN COMPLETE ✅
# ============================================================