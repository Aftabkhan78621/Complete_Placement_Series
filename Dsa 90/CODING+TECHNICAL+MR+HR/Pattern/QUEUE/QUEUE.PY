# ============================================================
# QUEUE - Batch 1 (Theory + Basic Questions)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY (Basic Interview Level)
# ============================================================

"""
WHAT IS A QUEUE?

A Queue is a Linear Data Structure that follows the FIFO
(First In, First Out) principle. It means the element inserted
first is removed first. Think of people standing in a ticket
counter queue. The person who comes first gets the ticket first.

Unlike Stack, Queue has two ends.

Front → Deletion (Dequeue)
Rear  → Insertion (Enqueue)

Example

Enqueue 10
Enqueue 20
Enqueue 30

Front                 Rear
-----------------------------
10        20        30

Now if we perform Dequeue(), 10 will be removed first.

------------------------------------------------------------

WHY DO WE USE QUEUE?

Queue is used whenever data should be processed in the same
order in which it arrives.

Examples:

• Ticket Booking
• Printer Queue
• CPU Scheduling
• BFS Traversal
• Call Center Systems
• Food Ordering Queue

------------------------------------------------------------

MEMORY REPRESENTATION

Queue can be implemented using

1. Array (Python List)
2. Linked List
3. collections.deque (Python)

For TCS Prime and Service-Based interviews,
Python List is sufficient to understand the concept.

Front                     Rear

10 ---> 20 ---> 30 ---> 40

------------------------------------------------------------

BASIC OPERATIONS

Enqueue()
Insert element at Rear.

Dequeue()
Remove element from Front.

Front()
Return first element.

Rear()
Return last element.

isEmpty()
Checks whether Queue is empty.

Size()
Returns number of elements.

------------------------------------------------------------

TIME COMPLEXITY

Enqueue      O(1)
Dequeue      O(n) using List
Front        O(1)
Rear         O(1)
isEmpty      O(1)
Size         O(1)

(Note:
Python List uses pop(0), so Dequeue becomes O(n).
collections.deque provides O(1), but List is enough
for interview basics.)

------------------------------------------------------------

ADVANTAGES

✔ Easy to understand
✔ Maintains insertion order
✔ Useful for scheduling
✔ FIFO processing

------------------------------------------------------------

DISADVANTAGES

✘ Middle elements cannot be accessed directly.
✘ Dequeue using List takes O(n).

------------------------------------------------------------

WHERE IS QUEUE USED?

• Ticket Booking
• Printer Queue
• CPU Scheduling
• BFS
• Networking
• Call Centers

------------------------------------------------------------

INTERVIEW QUESTIONS

1. What is Queue?
2. Explain FIFO.
3. Difference between Stack and Queue.
4. Enqueue vs Dequeue.
5. Applications of Queue.
6. Time Complexity.
7. Implement Queue in Python.

------------------------------------------------------------

PYTHON IMPLEMENTATION

queue = []

queue.append(10)      # Enqueue

queue.pop(0)          # Dequeue

queue[0]              # Front

queue[-1]             # Rear

------------------------------------------------------------

COMMON MISTAKES

✘ Using pop() instead of pop(0)
✘ Confusing FIFO with LIFO
✘ Removing from Rear
✘ Accessing empty Queue

This much theory is enough for
TCS Prime + Service-Based interviews.
"""


# ============================================================
# STEP 2 : BASIC QUESTIONS
# ============================================================


"""
Q1.
Implement Queue using Python List.

Queue can be implemented using a Python List. New elements are
inserted at the Rear using append(). Elements are removed from
the Front using pop(0). This is the simplest Queue implementation
and is commonly accepted for basic interview questions.
"""


"""
Q2.
Enqueue an Element.

Enqueue means inserting a new element at the Rear of the Queue.
Python's append() method performs this operation. Every new
element is added after the current Rear element while maintaining
FIFO order.
"""


"""
Q3.
Dequeue an Element.

Dequeue removes the Front element because Queue follows FIFO.
Python's pop(0) removes the first element from the list. Always
check whether the Queue is empty before calling pop(0) to avoid
IndexError.
"""


"""
Q4.
Front and Rear Element.

Front returns the first element without removing it.
Rear returns the last element without removing it.
These operations help us inspect the Queue while keeping its
contents unchanged.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

queue = []

# -------------------------
# Q1 Create Queue
# -------------------------

print("Initial Queue :", queue)

# -------------------------
# Q2 Enqueue
# -------------------------

queue.append(10)
queue.append(20)
queue.append(30)

print("After Enqueue :", queue)

# -------------------------
# Q3 Dequeue
# -------------------------

removed = queue.pop(0)

print("Removed Element :", removed)

print("Queue After Dequeue :", queue)

# -------------------------
# Q4 Front & Rear
# -------------------------

print("Front Element :", queue[0])

print("Rear Element :", queue[-1])

# Optional Operations

print("Queue Size :", len(queue))

print("Is Empty :", len(queue) == 0)


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Create Queue
Time  : O(1)
Space : O(1)

Enqueue
Time  : O(1)
Space : O(1)

Dequeue (List)
Time  : O(n)
Space : O(1)

Front
Time  : O(1)
Space : O(1)

Rear
Time  : O(1)
Space : O(1)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Queue follows FIFO (First In First Out).
✔ Insertion happens at Rear.
✔ Deletion happens at Front.
✔ append() = Enqueue
✔ pop(0) = Dequeue (List implementation)
✔ queue[0] = Front
✔ queue[-1] = Rear
✔ Queue is mainly used in scheduling and sequential processing.
✔ Frequently asked in TCS Prime & Service-Based interviews.
"""


# ============================================================
# QUEUE - Batch 1 COMPLETE ✅
# ============================================================
