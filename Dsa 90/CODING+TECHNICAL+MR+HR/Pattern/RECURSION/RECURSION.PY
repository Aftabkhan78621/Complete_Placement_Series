# ============================================================
# RECURSION - Batch 1 (Theory + Basic Questions)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY (Basic Interview Level)
# ============================================================

"""
WHAT IS RECURSION?

Recursion is a programming technique in which a function calls
itself to solve a smaller version of the same problem. Instead of
using loops, the function repeatedly calls itself until a stopping
condition is reached.

That stopping condition is called the Base Case.

Without a Base Case, the function keeps calling itself forever
and finally gives a RecursionError (Stack Overflow).

------------------------------------------------------------

REAL LIFE EXAMPLE

Think about standing between two mirrors.

Mirror
   ↓
Image
   ↓
Image
   ↓
Image
   ↓

The same image repeats again and again until it stops.

Recursion works in a similar way.

------------------------------------------------------------

HOW RECURSION WORKS?

Every recursive function has two parts.

1. Base Case
Stops recursion.

2. Recursive Case
Calls itself with a smaller problem.

Example

factorial(5)

↓

factorial(4)

↓

factorial(3)

↓

factorial(2)

↓

factorial(1)

↓

Stop (Base Case)

Now answers return back one by one.

------------------------------------------------------------

CALL STACK

Every recursive function call is stored inside the Call Stack.

Example

main()

↓

print(5)

↓

print(4)

↓

print(3)

↓

Base Case

Now execution returns in reverse order.

This is why Recursion internally uses Stack.

------------------------------------------------------------

WHEN DO WE USE RECURSION?

• Tree Traversal
• Graph DFS
• Binary Search
• Backtracking
• Divide and Conquer
• Mathematical Problems

------------------------------------------------------------

ADVANTAGES

✔ Easy to write.
✔ Small code.
✔ Good for Tree and Graph problems.
✔ Natural for Divide and Conquer.

------------------------------------------------------------

DISADVANTAGES

✘ Uses extra Stack memory.
✘ Can be slower than loops.
✘ Stack Overflow if Base Case is missing.

------------------------------------------------------------

TIME COMPLEXITY

Depends on the problem.

Simple recursion generally takes O(n).

------------------------------------------------------------

INTERVIEW QUESTIONS

1. What is Recursion?
2. What is Base Case?
3. What is Recursive Case?
4. What is Call Stack?
5. Difference between Loop and Recursion?
6. Advantages?
7. Disadvantages?

------------------------------------------------------------

COMMON MISTAKES

✘ Missing Base Case
✘ Infinite Recursion
✘ Wrong Recursive Call
✘ Forgetting Return Statement

This theory is enough for
TCS Prime + Service-Based interviews.
"""


# ============================================================
# STEP 2 : BASIC QUESTIONS
# ============================================================


"""
Q1. Print Numbers from 1 to N

This is the easiest recursion question. The function first reaches
the Base Case and while returning from recursion it prints numbers
from 1 to N. This question helps understand how recursive calls are
stored in the Call Stack.
"""


"""
Q2. Print Numbers from N to 1

This question is the reverse of the previous one. Here we print the
current number first and then call the recursive function. Since
printing happens before recursion, the output comes from N to 1.
"""


"""
Q3. Sum of First N Numbers

The function returns n + sum(n-1). Every recursive call adds one
number until the Base Case (0) is reached. While returning, all
values are added together to produce the final answer.
"""


"""
Q4. Factorial of a Number

Factorial means multiplying all numbers from 1 to n.

Example

5! = 5 × 4 × 3 × 2 × 1 = 120

The recursive formula is:

factorial(n) = n × factorial(n-1)

Base Case:
factorial(0) = 1
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

# -------------------------
# Q1 Print 1 to N
# -------------------------

def print_1_to_n(n):

    if n == 0:

        return

    print_1_to_n(n - 1)

    print(n, end=" ")


print("Print 1 to N :")

print_1_to_n(5)

print()


# -------------------------
# Q2 Print N to 1
# -------------------------

def print_n_to_1(n):

    if n == 0:

        return

    print(n, end=" ")

    print_n_to_1(n - 1)


print()

print("Print N to 1 :")

print_n_to_1(5)

print()


# -------------------------
# Q3 Sum of N Numbers
# -------------------------

def sum_n(n):

    if n == 0:

        return 0

    return n + sum_n(n - 1)


print()

print("Sum of First 5 Numbers :", sum_n(5))


# -------------------------
# Q4 Factorial
# -------------------------

def factorial(n):

    if n == 0:

        return 1

    return n * factorial(n - 1)


print()

print("Factorial of 5 :", factorial(5))


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Print 1 to N
Time  : O(n)
Space : O(n)

Print N to 1
Time  : O(n)
Space : O(n)

Sum of N Numbers
Time  : O(n)
Space : O(n)

Factorial
Time  : O(n)
Space : O(n)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Every recursive function must have a Base Case.
✔ Recursion internally uses the Call Stack.
✔ Recursive calls execute first, then return one by one.
✔ Missing Base Case causes Stack Overflow.
✔ Factorial is the most common recursion interview question.
✔ Print 1→N and N→1 help understand recursion flow.
✔ Frequently Asked in TCS Prime & Service-Based interviews.
"""


# ============================================================
# RECURSION - Batch 1 COMPLETE ✅
# ============================================================

# ============================================================
# RECURSION - Batch 2 (Basic Mathematical Problems)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY
# ============================================================

"""
Batch 2 me hum Recursion ke kuch important mathematical problems
seekhenge. In problems ka main purpose recursion flow, Base Case aur
Recursive Case ko aur achhi tarah samajhna hai.

Har problem me input har recursive call ke saath chhota hota jata hai
aur ek stage par Base Case aata hai. Uske baad function reverse order
me return hota hai. Fibonacci aur Power questions recursion ke sabse
common interview questions hain, jabki Count Digits aur Sum of Digits
number manipulation ko test karte hain.
"""


# ============================================================
# Q1. FIBONACCI NUMBER
# ============================================================

"""
Fibonacci Series me har number pichhle do numbers ka sum hota hai.

0 1 1 2 3 5 8 13 ...

Recursive formula:

F(n) = F(n-1) + F(n-2)

Base Cases:
F(0) = 0
F(1) = 1

Ye recursion ka classic interview question hai. Basic version
service-based companies me pucha ja sakta hai.
"""


# ============================================================
# Q2. POWER (xⁿ)
# ============================================================

"""
Power problem me x raised to n calculate karte hain.

Example:
2⁵ = 32

Recursive Formula:

power(x,n) = x × power(x,n-1)

Base Case:
power(x,0) = 1

Har recursive call exponent ko ek kam karta hai.
"""


# ============================================================
# Q3. COUNT DIGITS
# ============================================================

"""
Count Digits me kisi number me total digits count karni hoti hain.
Har recursive call me number ko 10 se divide karte hain, jisse ek
digit remove ho jati hai. Jab number 0 ho jata hai to recursion
stop ho jati hai.
"""


# ============================================================
# Q4. SUM OF DIGITS
# ============================================================

"""
Sum of Digits me last digit ko n % 10 se nikalte hain aur remaining
number ko n // 10 se recursive call me bhejte hain. Jab number 0 ho
jata hai to recursion stop ho jati hai aur saari digits ka sum
return hota hai.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

# -------------------------
# Q1 Fibonacci Number
# -------------------------

def fibonacci(n):

    if n <= 1:

        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci of 6 :")

print(fibonacci(6))


# -------------------------
# Q2 Power (xⁿ)
# -------------------------

def power(x, n):

    if n == 0:

        return 1

    return x * power(x, n - 1)


print()

print("2 Power 5 :")

print(power(2, 5))


# -------------------------
# Q3 Count Digits
# -------------------------

def count_digits(n):

    if n == 0:

        return 0

    return 1 + count_digits(n // 10)


number = 12345

print()

print("Count Digits :")

print(count_digits(number))


# -------------------------
# Q4 Sum of Digits
# -------------------------

def sum_digits(n):

    if n == 0:

        return 0

    return (n % 10) + sum_digits(n // 10)


print()

print("Sum of Digits :")

print(sum_digits(number))


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Fibonacci
Time  : O(2ⁿ)
Space : O(n)

Power
Time  : O(n)
Space : O(n)

Count Digits
Time  : O(log₁₀n)
Space : O(log₁₀n)

Sum of Digits
Time  : O(log₁₀n)
Space : O(log₁₀n)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Fibonacci has two recursive calls.
✔ Fibonacci basic recursion is not optimized.
✔ Power decreases exponent by one each call.
✔ Count Digits repeatedly divides by 10.
✔ Sum of Digits uses %10 and //10.
✔ Every recursive function must have a Base Case.
✔ Frequently Asked in TCS Prime & Service-Based interviews.
"""


# ============================================================
# RECURSION - Batch 2 COMPLETE ✅
# ============================================================

# ============================================================
# RECURSION - Batch 3 (String & Searching Problems)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY
# ============================================================

"""
Batch 3 me hum Recursion ke String aur Searching based questions
seekhenge. Ye questions recursion ke practical use ko samajhne ke
liye important hain.

Reverse String aur Palindrome Check recursion ke common string
questions hain. Binary Search ka recursive version divide-and-
conquer concept ko introduce karta hai. Decimal to Binary recursion
ka basic number conversion question hai.

Ye sabhi questions TCS Prime aur service-based interviews ke basic
level ke liye sufficient hain.
"""


# ============================================================
# Q1. REVERSE STRING
# ============================================================

"""
Reverse String me har recursive call first character ko skip karti
hai aur remaining string ko reverse karti hai. Jab string empty ho
jati hai, recursion stop hoti hai. Return ke time characters reverse
order me judte hain aur final reversed string mil jati hai.
"""


# ============================================================
# Q2. PALINDROME CHECK
# ============================================================

"""
Palindrome String wo hoti hai jo aage aur piche dono taraf se same
padhi jaye.

Example:
MADAM
LEVEL

Recursion me first aur last character compare karte hain. Agar dono
same hon to beech wali substring ke liye recursive call karte hain.
"""


# ============================================================
# Q3. BINARY SEARCH (RECURSIVE)
# ============================================================

"""
Recursive Binary Search sirf sorted array par work karta hai.
Har recursive call me search space half ho jata hai.

Target agar middle se chhota ho to left half me search karte hain,
warna right half me. Isliye Binary Search ki time complexity
O(log n) hoti hai.
"""


# ============================================================
# Q4. DECIMAL TO BINARY
# ============================================================

"""
Decimal number ko Binary me convert karne ke liye number ko baar-baar
2 se divide karte hain. Recursive call pehle quotient ke liye hoti
hai aur remainder (%2) return ke time print hota hai. Isse binary
digits sahi order me print hote hain.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

# -------------------------
# Q1 Reverse String
# -------------------------

def reverse_string(text):

    if text == "":

        return ""

    return reverse_string(text[1:]) + text[0]


print("Reverse String :")

print(reverse_string("HELLO"))


# -------------------------
# Q2 Palindrome Check
# -------------------------

def palindrome(text, left, right):

    if left >= right:

        return True

    if text[left] != text[right]:

        return False

    return palindrome(text, left + 1, right - 1)


word = "MADAM"

print()

print("Palindrome :")

print(palindrome(word, 0, len(word) - 1))


# -------------------------
# Q3 Recursive Binary Search
# -------------------------

def binary_search(arr, left, right, target):

    if left > right:

        return -1

    mid = (left + right) // 2

    if arr[mid] == target:

        return mid

    if target < arr[mid]:

        return binary_search(arr, left, mid - 1, target)

    return binary_search(arr, mid + 1, right, target)


arr = [10,20,30,40,50,60]

print()

print("Binary Search Index :")

print(binary_search(arr, 0, len(arr) - 1, 40))


# -------------------------
# Q4 Decimal to Binary
# -------------------------

def decimal_to_binary(n):

    if n == 0:

        return

    decimal_to_binary(n // 2)

    print(n % 2, end="")


print()

print()

print("Binary of 13 :")

decimal_to_binary(13)

print()


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Reverse String
Time  : O(n²)
Space : O(n)

Palindrome Check
Time  : O(n)
Space : O(n)

Binary Search
Time  : O(log n)
Space : O(log n)

Decimal to Binary
Time  : O(log n)
Space : O(log n)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Reverse String builds the answer while returning.
✔ Palindrome compares first and last characters.
✔ Binary Search works only on sorted arrays.
✔ Binary Search divides the search space into half.
✔ Decimal to Binary prints remainder while returning.
✔ Every recursive function must have a proper Base Case.
✔ Frequently Asked in TCS Prime & Service-Based interviews.
"""


# ============================================================
# RECURSION - Batch 3 COMPLETE ✅
# ============================================================

# ============================================================
# RECURSION - Batch 4 (Basic Interview Problems)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY
# ============================================================

"""
Ye Recursion ka final basic batch hai. Isme hum kuch important
interview problems cover karenge jo recursion ka practical use
dikhate hain.

Tower of Hanoi recursion ka classical problem hai aur interview me
iska basic concept pucha ja sakta hai. Recursive Array Sum, Maximum
Element aur Linear Search recursion ke through array processing ko
samjhate hain.

Ye batch complete karne ke baad Recursion ka basic interview syllabus
complete ho jayega.
"""


# ============================================================
# Q1. TOWER OF HANOI (Basic Idea)
# ============================================================

"""
Tower of Hanoi me hume disks ko Source Rod se Destination Rod tak
move karna hota hai. Ek time par sirf ek disk move ho sakti hai aur
badi disk ko chhoti disk ke upar nahi rakh sakte.

Solution Recursion se banta hai:
1. n-1 disks ko helper rod par move karo.
2. Largest disk ko destination par move karo.
3. n-1 disks ko destination par move karo.
"""


# ============================================================
# Q2. RECURSIVE ARRAY SUM
# ============================================================

"""
Recursive Array Sum me array ke har element ko recursively add kiya
jata hai. Har recursive call current element ko answer me add karti
hai aur next index ke liye function call karti hai. Base Case tab
aata hai jab index array ke end tak pahunch jata hai.
"""


# ============================================================
# Q3. MAXIMUM ELEMENT
# ============================================================

"""
Maximum Element recursion se find karne ke liye current element ko
remaining array ke maximum se compare karte hain. Har recursive call
problem ko chhota banati hai aur last element Base Case hota hai.
"""


# ============================================================
# Q4. LINEAR SEARCH
# ============================================================

"""
Recursive Linear Search me current index par target check karte hain.
Agar match mil jaye to index return karte hain, warna next index ke
liye recursive call karte hain. End tak pahunchne par -1 return hota
hai.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

# -------------------------
# Q1 Tower of Hanoi
# -------------------------

def tower_of_hanoi(n, source, helper, destination):

    if n == 1:

        print(source, "->", destination)

        return

    tower_of_hanoi(n - 1, source, destination, helper)

    print(source, "->", destination)

    tower_of_hanoi(n - 1, helper, source, destination)


print("Tower of Hanoi (2 Disks):")

tower_of_hanoi(2, "A", "B", "C")


# -------------------------
# Q2 Recursive Array Sum
# -------------------------

def array_sum(arr, index):

    if index == len(arr):

        return 0

    return arr[index] + array_sum(arr, index + 1)


arr = [10, 20, 30, 40]

print()

print("Array Sum :")

print(array_sum(arr, 0))


# -------------------------
# Q3 Maximum Element
# -------------------------

def maximum(arr, index):

    if index == len(arr) - 1:

        return arr[index]

    return max(arr[index], maximum(arr, index + 1))


print()

print("Maximum Element :")

print(maximum(arr, 0))


# -------------------------
# Q4 Recursive Linear Search
# -------------------------

def linear_search(arr, index, target):

    if index == len(arr):

        return -1

    if arr[index] == target:

        return index

    return linear_search(arr, index + 1, target)


print()

print("Linear Search Index :")

print(linear_search(arr, 0, 30))


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Tower of Hanoi
Time  : O(2ⁿ)
Space : O(n)

Recursive Array Sum
Time  : O(n)
Space : O(n)

Maximum Element
Time  : O(n)
Space : O(n)

Linear Search
Time  : O(n)
Space : O(n)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Tower of Hanoi is a classic recursion problem.
✔ Array Sum reduces the problem by one element each call.
✔ Maximum Element compares current value with recursive result.
✔ Linear Search checks one element per recursive call.
✔ Every recursive function must have a Base Case.
✔ Recursion internally uses the Call Stack.
✔ These are common basic recursion questions in
   TCS Prime & Service-Based interviews.
"""


# ============================================================
# RECURSION COMPLETE ✅
# ============================================================

