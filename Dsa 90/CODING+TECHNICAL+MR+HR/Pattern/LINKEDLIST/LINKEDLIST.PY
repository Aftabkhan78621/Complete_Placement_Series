# ============================================================
# LINKED LIST - Batch 1 (Theory + Basic Questions)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY (Basic Interview Level)
# ============================================================

"""
WHAT IS A LINKED LIST?

A Linked List is a Linear Data Structure in which elements are
stored in separate memory locations. Unlike an Array, elements
are not stored continuously. Every element is called a Node.

Each Node contains two parts:

1. Data
2. Next Pointer

The Next Pointer stores the address of the next node.

Example

Head
 ↓
+------+------+
| 10 |   •----|---->
+------+------+
              ↓
        +------+------+
        | 20 |   •----|---->
        +------+------+
                      ↓
                +------+------+
                | 30 |  None |
                +------+------+

------------------------------------------------------------

WHY DO WE USE LINKED LIST?

Arrays have fixed size and inserting or deleting elements in
the middle is expensive. Linked List solves this problem because
nodes can be inserted or deleted easily by changing pointers.

------------------------------------------------------------

REAL LIFE EXAMPLE

Think of a Treasure Hunt.

Each clue tells you where the next clue is hidden.

Current Clue ---> Next Clue ---> Next Clue ---> End

Exactly the same way every node stores the address of the next
node.

------------------------------------------------------------

MEMORY REPRESENTATION

Array

10 20 30 40
Stored together in continuous memory.

Linked List

10 --> 20 --> 30 --> 40 --> None

Every node can be stored anywhere in memory.

------------------------------------------------------------

IMPORTANT TERMS

Node
A single element of Linked List.

Head
The first node of the Linked List.

Next
Stores address of next node.

Tail
Last node whose next is None.

------------------------------------------------------------

TYPES OF LINKED LIST

1. Singly Linked List
Every node points to next node only.

2. Doubly Linked List
Every node has Previous and Next pointer.

3. Circular Linked List
Last node points to first node.

For TCS Prime, Singly Linked List is the most important.

------------------------------------------------------------

TIME COMPLEXITY

Traversal              O(n)
Insertion Beginning    O(1)
Insertion End          O(n)
Deletion Beginning     O(1)
Deletion End           O(n)
Searching              O(n)

------------------------------------------------------------

ADVANTAGES

✔ Dynamic Size
✔ Easy Insertion
✔ Easy Deletion
✔ Memory allocated when needed

------------------------------------------------------------

DISADVANTAGES

✘ Extra memory for pointer
✘ Cannot access by index
✘ Searching is slow

------------------------------------------------------------

APPLICATIONS

• Music Playlist
• Browser Navigation
• Undo/Redo
• Image Viewer
• Memory Management

------------------------------------------------------------

INTERVIEW QUESTIONS

1. What is Linked List?
2. Difference between Array & Linked List?
3. What is Node?
4. What is Head?
5. Types of Linked List?
6. Advantages?
7. Applications?

------------------------------------------------------------

COMMON MISTAKES

✘ Forgetting to update next pointer
✘ Losing head node
✘ Traversing until None incorrectly

This theory is sufficient for
TCS Prime + Service-Based interviews.
"""


# ============================================================
# STEP 2 : BASIC QUESTIONS
# ============================================================

"""
Q1. Create a Node

A Node is the building block of a Linked List. Every node stores
data and a reference (next) to the next node. If there is no next
node, next is None. Almost every Linked List problem starts by
creating a Node class.
"""


"""
Q2. Create a Linked List

A Linked List is created by connecting multiple nodes using the
next pointer. The first node is called the Head. The last node
always points to None. This is the basic structure of every
Singly Linked List.
"""


"""
Q3. Traverse a Linked List

Traversal means visiting every node one by one starting from the
Head until None is reached. A temporary pointer is generally used
so that the original Head is not modified during traversal.
"""


"""
Q4. Count Nodes

To count nodes, start from the Head and move to the next node until
None is reached. Increase the counter at every node. This is one
of the most common basic interview questions.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

# -------------------------
# Node Class
# -------------------------

class Node:

    def __init__(self, data):

        self.data = data

        self.next = None


# -------------------------
# Q1 Create Nodes
# -------------------------

first = Node(10)

second = Node(20)

third = Node(30)


# -------------------------
# Q2 Create Linked List
# -------------------------

first.next = second

second.next = third

head = first


# -------------------------
# Q3 Traverse Linked List
# -------------------------

print("Linked List :")

temp = head

while temp:

    print(temp.data, end=" -> ")

    temp = temp.next

print("None")


# -------------------------
# Q4 Count Nodes
# -------------------------

count = 0

temp = head

while temp:

    count += 1

    temp = temp.next

print()

print("Total Nodes :", count)


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Create Node
Time  : O(1)
Space : O(1)

Create Linked List
Time  : O(1)
Space : O(1)

Traversal
Time  : O(n)
Space : O(1)

Count Nodes
Time  : O(n)
Space : O(1)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Node = Data + Next Pointer
✔ Head points to first node.
✔ Last node always points to None.
✔ Linked List is not stored in contiguous memory.
✔ Traversal always starts from Head.
✔ Never modify Head directly while traversing.
✔ Singly Linked List is the most important for
   TCS Prime & Service-Based interviews.
"""


# ============================================================
# LINKED LIST - Batch 1 COMPLETE ✅
# ============================================================