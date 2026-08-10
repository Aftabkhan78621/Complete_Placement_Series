# ============================================================
# STACK - Batch 1 (Theory + Basic Questions)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY (Basic Interview Level)
# ============================================================

"""
WHAT IS A STACK?

A Stack is a Linear Data Structure that follows the LIFO
(Last In, First Out) principle. It means the element inserted
last will be removed first. Think of a stack of plates in a
kitchen. If you keep placing plates one over another, the last
plate placed on top is the first one you remove.

A Stack allows insertion and deletion only from one end,
called the TOP of the stack.

Example

Push 10
Push 20
Push 30

Stack
-------
30   <- TOP
20
10

Now if we remove an element (Pop), 30 will be removed first.

------------------------------------------------------------

WHY DO WE USE STACK?

Stack is used whenever we need to process data in reverse order
or remember previous operations.

Examples:
• Undo/Redo in MS Word
• Browser Back Button
• Function Calls
• Expression Evaluation
• Parentheses Matching
• DFS Traversal
• Backtracking Problems

------------------------------------------------------------

MEMORY REPRESENTATION

A Stack can be implemented using

1. Array (Python List)
2. Linked List

For service-based companies, Python List is enough.

Stack
---------
| 10 |
| 20 |
| 30 | <- TOP

------------------------------------------------------------

BASIC OPERATIONS

Push()
Insert an element on the top.

Pop()
Remove the top element.

Peek()/Top()
Return the top element without removing it.

isEmpty()
Checks whether stack is empty.

Size()
Returns total number of elements.

------------------------------------------------------------

TIME COMPLEXITY

Push      O(1)
Pop       O(1)
Peek      O(1)
isEmpty   O(1)
Size      O(1)

------------------------------------------------------------

ADVANTAGES

✔ Easy to implement
✔ Fast insertion and deletion
✔ Uses very little extra memory
✔ Best for reverse operations

------------------------------------------------------------

DISADVANTAGES

✘ Cannot access middle elements directly.
✘ Only top element can be accessed.
✘ Searching is O(n).

------------------------------------------------------------

WHERE IS STACK USED?

• Browser History
• Undo / Redo
• Function Calls
• Compiler
• Expression Evaluation
• Parentheses Matching
• DFS Algorithm
• Backtracking

------------------------------------------------------------

INTERVIEW QUESTIONS

1. What is Stack?
2. Explain LIFO.
3. Difference between Stack and Queue.
4. Push vs Pop.
5. Applications of Stack.
6. Time Complexity of Stack Operations.
7. Implement Stack in Python.

------------------------------------------------------------

PYTHON IMPLEMENTATION

Python List works as a Stack.

stack = []

stack.append(10)     # Push
stack.pop()          # Pop
stack[-1]            # Peek

------------------------------------------------------------

COMMON MISTAKES

✘ Using pop(0) instead of pop()
✘ Accessing empty stack
✘ Confusing Stack with Queue
✘ Forgetting to check isEmpty()

This much theory is sufficient for
TCS Prime + Service-Based interviews.
"""


# ============================================================
# STEP 2 : BASIC QUESTIONS
# ============================================================


"""
Q1.
Implement Stack using Python List.

This is the most basic Stack question. The interviewer checks
whether you know how to create a stack and perform operations
using Python's built-in list. Python list provides append() for
Push and pop() for Pop. This is the easiest and most commonly
accepted implementation in service-based company interviews.
"""

stack = []

# -------------------------
# Q1 Create Stack
# -------------------------

print("Initial Stack :", stack)

"""
Q2.
Push an Element into Stack.

Push means inserting a new element at the TOP of the stack.
Python's append() method performs Push in O(1) time because it
adds the element at the end of the list. Every new element
becomes the new TOP of the stack.
"""


# -------------------------
# Q2 Push Operation
# -------------------------

stack.append(10)
stack.append(20)
stack.append(30)

print("After Push :", stack)

"""
Q3.
Pop an Element from Stack.

Pop removes the TOP element from the stack. Since Stack follows
LIFO, the last inserted element is removed first. Python's pop()
removes the last element in constant time. Always check whether
the stack is empty before calling pop().
"""

# -------------------------
# Q3 Pop Operation
# -------------------------

removed = stack.pop()

print("Removed Element :", removed)

print("Stack After Pop :", stack)

"""
Q4.
Peek the Top Element.

Peek returns the TOP element without removing it. In Python,
stack[-1] returns the last element. This operation is useful
when we only need to inspect the current top value while keeping
the stack unchanged.
"""
# -------------------------
# Q4 Peek Operation
# -------------------------

print("Top Element :", stack[-1])

# Optional Operations

print("Size :", len(stack))

print("Is Empty :", len(stack) == 0)


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Create Stack
Time  : O(1)
Space : O(1)

Push
Time  : O(1)
Space : O(1)

Pop
Time  : O(1)
Space : O(1)

Peek
Time  : O(1)
Space : O(1)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Stack follows LIFO (Last In First Out).
✔ Insertion and deletion happen only at TOP.
✔ Python List is enough for implementation.
✔ append() = Push
✔ pop() = Pop
✔ stack[-1] = Peek
✔ Always check if stack is empty before Pop or Peek.
✔ One of the most frequently asked basic theory topics in
   TCS Prime and Service-Based interviews.
"""


# ============================================================
# STACK - Batch 1 COMPLETE ✅
# ============================================================


# ============================================================
# STACK - Batch 2 (Basic Interview Questions)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY
# ============================================================

"""
In Batch 1 humne Stack ka basic concept aur operations (Push, Pop,
Peek) dekhe. Ab Batch 2 me hum Stack ke basic interview questions
cover karenge jo service-based companies me frequently puche jate hain.

Is batch ka focus Stack ke applications aur simple problem solving par
hai. Yahan interviewer ye check karta hai ki tum Stack ko practically
use kar sakte ho ya nahi. Hum Python List ko Stack ki tarah use karenge
kyunki ye interview ke liye sufficient hai.

Ye batch complete karne ke baad tum Stack ke basic implementation
questions confidently solve kar paoge.
"""


# ============================================================
# Q1. DISPLAY STACK
# ============================================================

"""
Display Stack ka matlab Stack ke saare elements print karna hota hai.
Normally Stack ko Top se Bottom print kiya jata hai taaki current TOP
sabse pehle dikhe. Python me reverse traversal use karke easily Stack
display ki ja sakti hai.
"""
# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

stack = [10, 20, 30, 40, 50]

# -------------------------
# Q1 Display Stack
# -------------------------

print("Display Stack (Top to Bottom):")

for i in range(len(stack) - 1, -1, -1):

    print(stack[i])



# ============================================================
# Q2. SEARCH AN ELEMENT
# ============================================================

"""
Search operation me check karte hain ki given element Stack me present
hai ya nahi. Python List me 'in' operator se ye kaam aasani se ho
jata hai. Agar element mil jaye to True warna False return hota hai.
Service-based interviews me ye basic application question hai.
"""

# -------------------------
# Q2 Search Element
# -------------------------

element = 30

print()

if element in stack:

    print(element, "Found")

else:

    print(element, "Not Found")


# ============================================================
# Q3. IS STACK EMPTY
# ============================================================

"""
Pop ya Peek operation se pehle Stack empty hai ya nahi ye check karna
important hota hai. Empty Stack par Pop karne se error aata hai.
Python me len(stack) == 0 ya not stack dono valid approaches hain.
Ye interview ka bahut common theoretical question hai.
"""

# -------------------------
# Q3 Is Stack Empty
# -------------------------

print()

if len(stack) == 0:

    print("Stack is Empty")

else:

    print("Stack is Not Empty")




# ============================================================
# Q4. STACK SIZE
# ============================================================

"""
Stack Size ka matlab Stack me kitne elements present hain. Python me
len() function directly size return karta hai. Ye operation O(1) time
me hota hai aur Stack ke basic operations me include kiya jata hai.
"""
# -------------------------
# Q4 Stack Size
# -------------------------

print()

print("Stack Size :", len(stack))


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Display Stack
Time  : O(n)
Space : O(1)

Search Element
Time  : O(n)
Space : O(1)

Is Empty
Time  : O(1)
Space : O(1)

Stack Size
Time  : O(1)
Space : O(1)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Stack is displayed from Top to Bottom.
✔ 'in' operator performs linear search.
✔ Always check Empty before Pop/Peek.
✔ len(stack) gives Stack Size.
✔ not stack also checks if Stack is empty.
✔ Frequently Asked in TCS Prime & Service-Based Companies.
"""


# ============================================================
# STACK - Batch 2 COMPLETE ✅
# ============================================================

# ============================================================
# STACK - Batch 3 (Applications of Stack)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY
# ============================================================

"""
Ab tak hum Stack ke basic operations seekh chuke hain. Is batch me
hum Stack ke sabse common interview applications dekhenge. Service-
based companies generally advanced Stack algorithms nahi puchti, lekin
ye basic applications zarur puch sakti hain.

Stack ka use tab hota hai jab hume latest data ko pehle process karna
ho (LIFO). Browser Back, Undo/Redo, Reverse String aur Balanced
Parentheses Stack ke sabse famous applications hain. Agar ye concepts
clear hain to basic Stack theory complete mani jati hai.
"""


# ============================================================
# Q1. REVERSE A STRING
# ============================================================

"""
String ko reverse karne ke liye har character ko Stack me Push karte
hain. Uske baad Pop operation se characters reverse order me milte
hain aur reversed string ban jati hai. Ye Stack ka sabse basic
application hai aur LIFO concept ko clearly demonstrate karta hai.
"""


# ============================================================
# Q2. BALANCED PARENTHESES
# ============================================================

"""
Balanced Parentheses me opening brackets Stack me Push kiye jate hain.
Closing bracket aane par Stack ke Top se matching opening bracket Pop
kiya jata hai. Agar end me Stack empty ho to expression balanced hota
hai. Ye Stack ka sabse frequently asked interview question hai.
"""


# ============================================================
# Q3. BROWSER BACK HISTORY
# ============================================================

"""
Browser Back feature Stack ka real-life example hai. Har new page ko
Stack me Push kiya jata hai. Jab user Back button press karta hai to
latest page Pop ho jata hai aur previous page open ho jata hai. Isse
LIFO principle practically samajh aata hai.
"""


# ============================================================
# Q4. UNDO OPERATION
# ============================================================

"""
Text editors me Undo feature bhi Stack par based hota hai. Har action
Stack me save hota hai. Undo karne par latest action Stack se remove
hota hai aur previous state restore ho jati hai. Ye Stack ka common
application hai jo interviews me theory question ke roop me pucha
jata hai.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

# -------------------------
# Q1 Reverse String
# -------------------------

text = "STACK"

stack = []

for ch in text:

    stack.append(ch)

reverse = ""

while stack:

    reverse += stack.pop()

print("Reverse String :", reverse)


# -------------------------
# Q2 Balanced Parentheses
# -------------------------

expression = "{[()]}"

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

balanced = True

for ch in expression:

    if ch in "([{":

        stack.append(ch)

    else:

        if not stack or stack.pop() != pairs[ch]:

            balanced = False

            break

if balanced and not stack:

    print("Balanced")

else:

    print("Not Balanced")


# -------------------------
# Q3 Browser Back
# -------------------------

history = []

history.append("Google")

history.append("YouTube")

history.append("ChatGPT")

print("Current Page :", history[-1])

history.pop()

print("After Back :", history[-1])


# -------------------------
# Q4 Undo Operation
# -------------------------

actions = []

actions.append("Type A")

actions.append("Type B")

actions.append("Delete")

print("Undo :", actions.pop())


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Reverse String
Time  : O(n)
Space : O(n)

Balanced Parentheses
Time  : O(n)
Space : O(n)

Browser Back
Time  : O(1)
Space : O(n)

Undo Operation
Time  : O(1)
Space : O(n)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Reverse String is the simplest Stack application.
✔ Balanced Parentheses is the most asked Stack problem.
✔ Browser Back follows LIFO.
✔ Undo/Redo uses Stack internally.
✔ Push = append(), Pop = pop().
✔ Stack is mainly used where reverse processing is required.
"""


# ============================================================
# STACK - Batch 3 COMPLETE ✅
# ============================================================



# ============================================================
# STACK - Batch 4 (Interview Problems)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY
# ============================================================

"""
Is batch me hum Stack ke kuch basic interview problems dekhenge.
Ye problems Stack ka concept clear karne ke liye kaafi hain aur
TCS Prime aur service-based companies me isi level tak questions
aate hain.

Is batch ke baad tum Stack ko implement bhi kar paoge aur uske
common interview applications bhi solve kar loge. Advanced topics
jaise Monotonic Stack, Next Greater Element aur Histogram Problems
service-based interviews me rarely puche jate hain, isliye unhe
abhi skip kar rahe hain.
"""


# ============================================================
# Q1. COPY STACK
# ============================================================

"""
Kabhi-kabhi Stack ki original values ko bina change kiye uski copy
banana hota hai. Python me copy() method se easily duplicate Stack
ban sakti hai. Original aur copied Stack alag objects hote hain.
"""


# ============================================================
# Q2. CLEAR STACK
# ============================================================

"""
Clear Stack ka matlab Stack ke sabhi elements remove karna hota hai.
Python me clear() method use ki jati hai. Iske baad Stack empty ho
jati hai aur uska size zero ho jata hai.
"""


# ============================================================
# Q3. MULTIPLE PUSH
# ============================================================

"""
Interview me ek saath multiple elements Stack me insert karne ko
bola ja sakta hai. Iske liye loop use karke har element ko append()
ki madad se Push karte hain. Har new element Stack ke TOP par chala
jata hai.
"""


# ============================================================
# Q4. POP ALL ELEMENTS
# ============================================================

"""
Kabhi poori Stack ko empty karna hota hai aur saare elements LIFO
order me print karne hote hain. Jab tak Stack empty na ho, Pop
operation repeat karte rehte hain. Ye Stack ke LIFO behavior ko
demonstrate karta hai.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

stack = [10, 20, 30]

# -------------------------
# Q1 Copy Stack
# -------------------------

copy_stack = stack.copy()

print("Original Stack :", stack)
print("Copied Stack   :", copy_stack)


# -------------------------
# Q2 Clear Stack
# -------------------------

temp = stack.copy()

temp.clear()

print()
print("After Clear :", temp)


# -------------------------
# Q3 Multiple Push
# -------------------------

stack = []

elements = [5, 10, 15, 20]

for num in elements:

    stack.append(num)

print()
print("After Multiple Push :", stack)


# -------------------------
# Q4 Pop All Elements
# -------------------------

print()
print("Pop All Elements :")

while stack:

    print(stack.pop(), end=" ")


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Copy Stack
Time  : O(n)
Space : O(n)

Clear Stack
Time  : O(n)
Space : O(1)

Multiple Push
Time  : O(n)
Space : O(n)

Pop All Elements
Time  : O(n)
Space : O(1)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ copy() creates a separate Stack.
✔ clear() removes all elements.
✔ Multiple Push uses append() inside a loop.
✔ Pop All demonstrates LIFO order.
✔ Push, Pop and Peek remain O(1).
✔ Stack basics are now complete for TCS Prime &
   Service-Based interviews.
"""


# ============================================================
# STACK - COMPLETE ✅
# ============================================================