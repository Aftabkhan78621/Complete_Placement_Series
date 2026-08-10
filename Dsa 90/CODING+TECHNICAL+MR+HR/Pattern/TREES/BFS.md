# ==========================================================
#          BFS (Level Order Traversal) – Complete Notes
# ==========================================================

# ----------------------------------------------------------
# 1. What is BFS?
# ----------------------------------------------------------

BFS (Breadth First Search), also called Level Order Traversal, is a tree traversal
technique that visits nodes level by level from top to bottom and from left to right.
Instead of going deep into one branch first, BFS finishes all nodes of the current
level before moving to the next level.

Example Tree

            A
          /   \
         B     C
        / \   / \
       D   E F   G

Traversal

A → B → C → D → E → F → G

BFS always starts from the root node and processes one complete level before
continuing to the next level.

# ----------------------------------------------------------
# 2. Real-Life Example
# ----------------------------------------------------------

Imagine a school assembly where students are standing in rows.

Principal

Row 1
A

Row 2
B      C

Row 3
D  E   F  G

The principal greets students row by row.

Hello A
Hello B
Hello C
Hello D
Hello E
Hello F
Hello G

The principal does not greet one student's entire branch first.
Instead, every student in one row is greeted before moving to the next row.

This is exactly how BFS works.

# ----------------------------------------------------------
# 3. Why Do We Need BFS?
# ----------------------------------------------------------

Suppose you are searching for your friend inside a building.

Floor 1
Reception

Floor 2
Room 1      Room 2

Floor 3
Room 3   Room 4   Room 5   Room 6

Normally, you search every room on Floor 1 first, then Floor 2, and finally Floor 3.
You do not directly go to the deepest room.

BFS follows the same idea by searching level by level.

# ----------------------------------------------------------
# 4. DFS vs BFS
# ----------------------------------------------------------

Example Tree

            A
          /   \
         B     C
        / \   / \
       D   E F   G

DFS (Depth First Search)

A
B
D
E
C
F
G

DFS first goes as deep as possible into one branch before coming back.

BFS (Breadth First Search)

A
B
C
D
E
F
G

BFS completes one entire level before moving to the next level.

Difference

DFS
• Goes deep first.
• Uses Stack or Recursion.

BFS
• Goes level by level.
• Uses Queue.

# ----------------------------------------------------------
# 5. Why Can't We Use Recursion Easily?
# ----------------------------------------------------------

Suppose we start from node A.

After visiting A, we must remember to visit B and C later.

After visiting B, we must still remember C while also remembering D and E.

We need a data structure that stores nodes in the same order in which they arrive.

That data structure is called a Queue.

Recursion naturally follows one branch deeply, so it is suitable for DFS but not for
normal BFS.

# ----------------------------------------------------------
# 6. What is a Queue?
# ----------------------------------------------------------

Queue is a linear data structure that follows FIFO.

FIFO means

First In
First Out

The first element inserted into the queue is the first element removed.

Real-Life Example

Movie Ticket Counter

People arrive

A
B
C

Queue

Front

A  B  C

Back

Who gets the ticket first?

A

Then

B

Then

C

Exactly the same principle is used in BFS.

# ----------------------------------------------------------
# 7. Queue Operations
# ----------------------------------------------------------

Enqueue

Adds an element to the rear (back) of the queue.

Example

Queue

10

Enqueue 20

Queue

10 20

Dequeue

Removes the front element from the queue.

Example

Queue

10 20 30

↓

20 30

Python Queue Operations

append()

Adds a node to the back.

popleft()

Removes a node from the front.

Both operations take O(1) time using deque.

# ----------------------------------------------------------
# 8. How BFS Uses Queue
# ----------------------------------------------------------

Example Tree

            A
          /   \
         B     C
        / \   / \
       D   E F   G

Initially

Queue

[A]

Output

Empty

Step 1

Remove A

Print

A

Insert children

B
C

Queue

[B C]

--------------------------------------------------

Step 2

Remove B

Print

A B

Insert children

D
E

Queue

[C D E]

--------------------------------------------------

Step 3

Remove C

Print

A B C

Insert children

F
G

Queue

[D E F G]

--------------------------------------------------

Step 4

Remove D

Print

A B C D

Queue

[E F G]

--------------------------------------------------

Step 5

Remove E

Print

A B C D E

Queue

[F G]

--------------------------------------------------

Step 6

Remove F

Print

A B C D E F

Queue

[G]

--------------------------------------------------

Step 7

Remove G

Print

A B C D E F G

Queue

[]

Queue becomes empty.

Traversal stops.

# ----------------------------------------------------------
# 9. BFS Algorithm
# ----------------------------------------------------------

Step 1

Put the root node into the queue.

Step 2

While the queue is not empty

• Remove the front node.
• Print or process that node.
• Insert its left child (if present).
• Insert its right child (if present).

Step 3

Repeat until the queue becomes empty.

# ----------------------------------------------------------
# 10. Visual Flow
# ----------------------------------------------------------

Queue

[A]

↓

Remove A

↓

Print A

↓

Insert B C

↓

Queue

[B C]

↓

Remove B

↓

Print B

↓

Insert D E

↓

Queue

[C D E]

↓

Remove C

↓

Print C

↓

Insert F G

↓

Queue

[D E F G]

↓

Continue until the queue becomes empty.

# ----------------------------------------------------------
# 11. Why Queue and Not Stack?
# ----------------------------------------------------------

Queue processes nodes in FIFO order.

Oldest inserted node is processed first.

This naturally produces level-by-level traversal.

Stack processes nodes in LIFO order.

Newest inserted node is processed first.

This naturally produces Depth First Search.

Therefore

BFS → Queue

DFS → Stack / Recursion

# ----------------------------------------------------------
# 12. Python Implementation
# ----------------------------------------------------------

Python uses deque from the collections module because it provides efficient queue
operations.

Important Methods

append(node)

Adds a node at the back.

popleft()

Removes a node from the front.

Both operations are O(1).

# ----------------------------------------------------------
# 13. Dry Run
# ----------------------------------------------------------

Queue Before      Removed      Output          Queue After

[1]                  1           1             [2,3]

[2,3]                2           1 2           [3,4,5]

[3,4,5]              3           1 2 3         [4,5,6,7]

[4,5,6,7]            4           1 2 3 4       [5,6,7]

[5,6,7]              5           1 2 3 4 5     [6,7]

[6,7]                6           1 2 3 4 5 6   [7]

[7]                  7           1 2 3 4 5 6 7 []

Queue becomes empty.

Traversal ends.

# ----------------------------------------------------------
# 14. Time Complexity
# ----------------------------------------------------------

Time Complexity

O(n)

Reason

Every node is inserted into the queue once and removed once.

Each node is visited exactly one time.

# ----------------------------------------------------------
# 15. Space Complexity
# ----------------------------------------------------------

Space Complexity

O(w)

where

w = Maximum width of the tree

Reason

The queue stores all nodes of the widest level.

Worst Case

If the last level contains almost all nodes,

Space Complexity becomes

O(n)

# ----------------------------------------------------------
# 16. Applications of BFS
# ----------------------------------------------------------

• Level Order Traversal
• Printing nodes level by level
• Finding minimum depth of a binary tree
• Shortest path in an unweighted graph
• Network broadcasting
• Social network friend search
• GPS shortest route (unweighted)
• Web crawling

# ----------------------------------------------------------
# 17. Common Interview Mistakes
# ----------------------------------------------------------

❌ Forgetting to check if root is None.

❌ Using list.pop(0) instead of deque.popleft().

❌ Forgetting to insert left child.

❌ Forgetting to insert right child.

❌ Using Stack instead of Queue.

❌ Thinking BFS uses recursion.

# ----------------------------------------------------------
# 18. Interview Questions
# ----------------------------------------------------------

Q1. What is BFS?

Breadth First Search is a traversal technique that visits nodes level by level.

--------------------------------------------------

Q2. Which data structure is used in BFS?

Queue (FIFO).

--------------------------------------------------

Q3. Why Queue?

Because Queue processes the oldest inserted node first, allowing level-by-level
traversal.

--------------------------------------------------

Q4. Why not Stack?

Stack follows LIFO and naturally performs DFS.

--------------------------------------------------

Q5. Time Complexity?

O(n)

--------------------------------------------------

Q6. Space Complexity?

O(w)

Worst Case

O(n)

--------------------------------------------------

Q7. Where is BFS used?

Level Order Traversal

Shortest Path in Unweighted Graph

Minimum Depth

Network Routing

Graph Traversal

# ----------------------------------------------------------
# 19. Interview Variations (Very Important)
# ----------------------------------------------------------

These problems are based on the same BFS concept.

• Print each level on a new line.

Example

1

2 3

4 5 6 7

--------------------------------------------------

Return Levels

Output

[[1],
 [2,3],
 [4,5,6,7]]

--------------------------------------------------

LeetCode Problems

102. Binary Tree Level Order Traversal

107. Binary Tree Level Order Traversal II

637. Average of Levels in Binary Tree

199. Binary Tree Right Side View

# ----------------------------------------------------------
# 20. Quick Revision
# ----------------------------------------------------------

BFS

↓

Breadth First Search

↓

Uses Queue

↓

FIFO

↓

Visit Level by Level

↓

Root

↓

Left Child

↓

Right Child

↓

Repeat Until Queue Becomes Empty

Time Complexity

O(n)

Space Complexity

O(w)

Worst Case

O(n)

Used For

✓ Level Order Traversal

✓ Minimum Depth

✓ Shortest Path (Unweighted Graph)

✓ Graph Traversal

✓ Network Search

✓ Interview Coding Questions