# ============================================================
# HEAP & GRAPH (Basic Theory)
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. HEAP
# ============================================================

"""
WHAT IS A HEAP?

A Heap is a Special Binary Tree that follows the Heap Property.
It is also a Complete Binary Tree, which means every level is
completely filled except possibly the last level, and the last
level is filled from left to right.

Heap is mainly used when we need to quickly find the smallest
or largest element.

------------------------------------------------------------

TYPES OF HEAP

1. Min Heap
Parent <= Children

Smallest element is always at the Root.

Example

          10
        /    \
      20      30
     /  \
   40   50

------------------------------------------------------------

2. Max Heap
Parent >= Children

Largest element is always at the Root.

Example

          50
        /    \
      40      30
     /  \
   20    10

------------------------------------------------------------

IMPORTANT POINTS

✔ Heap is a Complete Binary Tree.
✔ Heap is NOT a Binary Search Tree (BST).
✔ Only Parent-Child relationship is maintained.
✔ Left child is not always smaller than right child.

------------------------------------------------------------

OPERATIONS

1. Insert
Insert new element and adjust Heap.

2. Delete
Delete Root and rearrange Heap.

3. Peek
Return Root element.

4. Heapify
Convert a Binary Tree into a Heap.

------------------------------------------------------------

TIME COMPLEXITY

Insert          O(log n)
Delete          O(log n)
Peek            O(1)
Heapify         O(n)

------------------------------------------------------------

APPLICATIONS

✔ Priority Queue
✔ CPU Scheduling
✔ Job Scheduling
✔ Dijkstra Algorithm
✔ Heap Sort
✔ Task Scheduling

------------------------------------------------------------

ADVANTAGES

✔ Fast insertion
✔ Fast deletion
✔ Quick access to Min/Max
✔ Efficient Priority Queue

------------------------------------------------------------

DISADVANTAGES

✘ Searching is O(n)
✘ Random access is not possible

------------------------------------------------------------

INTERVIEW QUESTIONS

1. What is Heap?
2. Difference between Min Heap and Max Heap?
3. What is Heap Property?
4. What is Complete Binary Tree?
5. Heap vs BST?
6. Heap Applications?
7. Time Complexity of Heap Operations?

------------------------------------------------------------

COMMON MISTAKES

✘ Heap is NOT BST.
✘ Only Parent-Child relation matters.
✘ Complete Binary Tree ≠ Perfect Binary Tree.

This much theory is sufficient for
TCS Prime + Service-Based Interviews.
"""


# ============================================================
# 2. PRIORITY QUEUE
# ============================================================

"""
WHAT IS PRIORITY QUEUE?

Priority Queue is a Queue where elements are processed according
to Priority instead of FIFO.

Example

Emergency Patient
VIP Patient
Normal Patient

Emergency Patient will be served first.

Heap is used to implement Priority Queue efficiently.

------------------------------------------------------------

OPERATIONS

Insert
Delete Highest/Lowest Priority
Peek Highest/Lowest Priority

------------------------------------------------------------

APPLICATIONS

✔ Hospital Management
✔ CPU Scheduling
✔ Network Routing
✔ Operating System
✔ Task Scheduling

------------------------------------------------------------

TIME COMPLEXITY

Insert      O(log n)
Delete      O(log n)
Peek        O(1)
"""


# ============================================================
# 3. GRAPH
# ============================================================

"""
WHAT IS A GRAPH?

Graph is a Non-Linear Data Structure consisting of Nodes
(Vertices) and Connections (Edges).

Graphs are used whenever relationships between objects need
to be represented.

Example

        A
      /   \
     B-----C
      \
       D

------------------------------------------------------------

TERMINOLOGY

Vertex
A Node in Graph.

Edge
Connection between two Vertices.

Degree
Number of edges connected to a vertex.

Path
Sequence of connected vertices.

Cycle
A path that starts and ends at the same vertex.

------------------------------------------------------------

TYPES OF GRAPH

1. Directed Graph

A -----> B

Direction matters.

----------------------------

2. Undirected Graph

A ------- B

No direction.

----------------------------

3. Weighted Graph

Edges contain weights.

A --5--> B

----------------------------

4. Unweighted Graph

Edges have no weight.

------------------------------------------------------------

GRAPH REPRESENTATION

1. Adjacency Matrix

Stores Graph using a 2D Matrix.

Advantages

✔ Easy implementation

Disadvantages

✘ Uses more memory.

----------------------------

2. Adjacency List

Stores neighbours of every node.

Advantages

✔ Memory Efficient
✔ Most commonly used

------------------------------------------------------------

GRAPH TRAVERSAL

1. BFS (Breadth First Search)

Uses Queue.

Visits nodes level by level.

Example

A

↓

B C

↓

D E

------------------------------------------------------------

2. DFS (Depth First Search)

Uses Stack or Recursion.

Explores one complete path before returning.

------------------------------------------------------------

TIME COMPLEXITY

Adjacency List

BFS     O(V + E)

DFS     O(V + E)

V = Vertices
E = Edges

------------------------------------------------------------

APPLICATIONS

✔ Google Maps
✔ Facebook Friends
✔ Instagram Followers
✔ Flight Routes
✔ Computer Networks
✔ Recommendation Systems
✔ GPS Navigation

------------------------------------------------------------

ADVANTAGES

✔ Represents complex relationships.
✔ Efficient traversal.
✔ Real-world modelling.

------------------------------------------------------------

DISADVANTAGES

✘ Can become complex.
✘ Traversal requires careful implementation.

------------------------------------------------------------

INTERVIEW QUESTIONS

1. What is Graph?
2. Vertex vs Edge?
3. Directed vs Undirected Graph?
4. BFS vs DFS?
5. Queue is used in?
6. Stack is used in?
7. Adjacency Matrix vs Adjacency List?
8. Applications of Graph?

------------------------------------------------------------

COMMON MISTAKES

✘ Tree is not always a Graph.
✘ BFS uses Queue.
✘ DFS uses Stack/Recursion.
✘ Graph may contain Cycles.

This theory is sufficient for
TCS Prime + Service-Based Interviews.
"""


# ============================================================
# FINAL INTERVIEW NOTES
# ============================================================

"""
HEAP

✔ Complete Binary Tree
✔ Min Heap
✔ Max Heap
✔ Heap Property
✔ Priority Queue
✔ Insert O(log n)
✔ Delete O(log n)
✔ Peek O(1)

------------------------------------------------------------

GRAPH

✔ Vertex
✔ Edge
✔ Directed Graph
✔ Undirected Graph
✔ Weighted Graph
✔ Adjacency Matrix
✔ Adjacency List
✔ BFS → Queue
✔ DFS → Stack / Recursion
✔ BFS & DFS = O(V + E)

------------------------------------------------------------

This is enough for TCS Prime, Infosys, Accenture,
Capgemini, Cognizant, Wipro, HCL, IBM, Deloitte,
and Cyntexa basic interviews.
"""

# ============================================================
# DSA COMPLETE ✅
# ============================================================