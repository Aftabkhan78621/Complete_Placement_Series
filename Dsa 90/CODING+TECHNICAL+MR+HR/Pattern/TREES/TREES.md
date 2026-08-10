# ============================================================
# TREES - Batch 1 (Theory + Basic Questions)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# STEP 1 : THEORY (Basic Interview Level)
# ============================================================

"""
WHAT IS A TREE?

A Tree is a Non-Linear Data Structure that stores data in a
hierarchical form. Unlike Array and Linked List, data is not
stored in a straight line. Every element is called a Node and
nodes are connected through edges.

Example

          10
         /  \
       20    30
      / \      \
    40  50     60

------------------------------------------------------------

WHY DO WE USE TREE?

Tree is used whenever data naturally forms a hierarchy.

Examples

• File System
• Company Organization Chart
• Family Tree
• HTML DOM
• Menu Structure

------------------------------------------------------------

IMPORTANT TERMINOLOGY

Root
The first node of the tree.

Parent
A node that has children.

Child
A node connected below a parent.

Sibling
Nodes having the same parent.

Leaf Node
A node having no children.

Internal Node
A node having at least one child.

Height
Longest path from Root to Leaf.

Depth
Distance from Root to a node.

Level
Position of a node from the Root.

------------------------------------------------------------

TYPES OF TREES

1. Binary Tree
Maximum two children.

2. Binary Search Tree (BST)
Left < Root < Right

3. Complete Tree
Every level filled except possibly last.

For TCS Prime, Binary Tree basics are sufficient.

------------------------------------------------------------

ADVANTAGES

✔ Hierarchical storage.
✔ Fast searching (BST concept).
✔ Dynamic structure.

------------------------------------------------------------

DISADVANTAGES

✘ More memory because of pointers.
✘ More difficult than Array.

------------------------------------------------------------

APPLICATIONS

• File Explorer
• XML / HTML
• Database Indexing (Basic Idea)
• Expression Trees

------------------------------------------------------------

INTERVIEW QUESTIONS

1. What is Tree?
2. What is Root?
3. What is Leaf Node?
4. Difference between Tree and Linked List?
5. What is Binary Tree?
6. What is BST?

------------------------------------------------------------

COMMON MISTAKES

✘ Confusing Height and Depth.
✘ Thinking every Tree is BST.
✘ Forgetting Leaf Node definition.

This theory is enough for
TCS Prime + Service-Based interviews.
"""


# ============================================================
# STEP 2 : BASIC QUESTIONS
# ============================================================

"""
Q1. Create Tree Node

Every Tree is built using Nodes. A Binary Tree Node contains
three parts:
1. Data
2. Left Child
3. Right Child
"""


"""
Q2. Build a Simple Binary Tree

Nodes are connected using left and right references.
The first node is called the Root.
"""


"""
Q3. Print Root

The Root is the starting node of the Tree.
It can be accessed directly using root.data.
"""


"""
Q4. Print Left and Right Child

Every Binary Tree node can have maximum two children.
They are accessed using root.left and root.right.
"""


# ============================================================
# STEP 3 : ONE BLOCK OF CODE
# ============================================================

class TreeNode:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None


# -------------------------
# Q1 Create Nodes
# -------------------------

root = TreeNode(10)

left = TreeNode(20)

right = TreeNode(30)


# -------------------------
# Q2 Build Tree
# -------------------------

root.left = left

root.right = right


# -------------------------
# Q3 Print Root
# -------------------------

print("Root Node :", root.data)


# -------------------------
# Q4 Print Children
# -------------------------

print("Left Child :", root.left.data)

print("Right Child :", root.right.data)


# ============================================================
# STEP 4 : COMPLEXITY
# ============================================================

"""
Create Node
Time  : O(1)
Space : O(1)

Build Tree
Time  : O(1)
Space : O(1)

Print Root
Time  : O(1)
Space : O(1)

Print Children
Time  : O(1)
Space : O(1)
"""


# ============================================================
# STEP 5 : INTERVIEW POINTS
# ============================================================

"""
✔ Tree is a Non-Linear Data Structure.
✔ Root is the first node.
✔ Leaf node has no children.
✔ Binary Tree has at most two children.
✔ Every BST is a Binary Tree, but every Binary Tree is not a BST.
✔ Root → Left → Right are basic references.
✔ Frequently Asked in TCS Prime & Service-Based interviews.
"""


# ============================================================
# TREES - Batch 1 COMPLETE ✅
# ============================================================


# ============================================================
# CHAPTER 1 : TREE BASICS
# ============================================================

# ------------------------------------------------------------
# 1. Tree
# ------------------------------------------------------------
# Definition:
# Tree is a non-linear data structure.
# It stores data in Parent -> Child relationship.

# Example:
#
#         A
#       /   \
#      B     C
#     / \     \
#    D   E     F
#

# ------------------------------------------------------------
# 2. Node
# ------------------------------------------------------------
# Every element in a tree is called a Node.

# Example:
# A, B, C, D, E, F are all Nodes.

# ------------------------------------------------------------
# 3. Root Node
# ------------------------------------------------------------
# Top-most node of the tree.
#
# Example:
#
#         A
#       /   \
#      B     C
#
# Root = A

# ------------------------------------------------------------
# 4. Parent Node
# ------------------------------------------------------------
# A node having one or more children.

# Example:
#
# A
# |
# B
#
# Parent = A

# ------------------------------------------------------------
# 5. Child Node
# ------------------------------------------------------------
# Node connected below a Parent.

# Example:
#
# A
# |
# B
#
# Child = B

# ------------------------------------------------------------
# 6. Leaf Node
# ------------------------------------------------------------
# Node having NO children.

# Example:
#
#         A
#       /   \
#      B     C
#     / \     \
#    D   E     F
#
# Leaf Nodes:
# D
# E
# F

# ------------------------------------------------------------
# 7. Internal Node
# ------------------------------------------------------------
# Node having at least one child.

# Example:
# A
# B
# C

# ------------------------------------------------------------
# 8. Edge
# ------------------------------------------------------------
# Connection between two nodes.

# Formula:
# Edges = Nodes - 1

# ------------------------------------------------------------
# 9. Level
# ------------------------------------------------------------
#
# Level 0 : A
# Level 1 : B C
# Level 2 : D E F

# ------------------------------------------------------------
# 10. Height
# ------------------------------------------------------------
# Longest path (in edges) from Root to Leaf.

# Example:
#
# A
# |
# B
# |
# C
#
# Height = 2

# ------------------------------------------------------------
# 11. Binary Tree
# ------------------------------------------------------------
# Every node can have at most 2 children.

# Valid:
#
#      A
#     / \
#    B   C
#
# Invalid:
#
#      A
#    / | \
#   B  C  D

# ------------------------------------------------------------
# Interview Points
# ------------------------------------------------------------
# 1. Root = Top-most node
# 2. Leaf = No children
# 3. Internal = Has child
# 4. Height = Longest path (edges)
# 5. Binary Tree = Max 2 children
# 6. Edges = Nodes - 1
# ============================================================


# ============================================================
# CHAPTER : TREE TRAVERSALS
# PREORDER | INORDER | POSTORDER
# ============================================================

# ============================================================
# 1. PREORDER
# ============================================================

# Rule:
# Root -> Left -> Right

# Shortcut:
# R L R

# Code:

def preorder(root):

    if root is None:
        return

    print(root.val, end=" ")

    preorder(root.left)

    preorder(root.right)


# Example:
#
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
#
# Output:
#
# 1 2 4 5 3 6 7
#
# Memory Trick:
# Parent First


# ============================================================
# 2. INORDER
# ============================================================

# Rule:
# Left -> Root -> Right

# Shortcut:
# L R R
# (Left, Root, Right)

# Code:

def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.val, end=" ")

    inorder(root.right)


# Example:
#
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
#
# Output:
#
# 4 2 5 1 6 3 7
#
# Memory Trick:
# Parent Middle


# ============================================================
# 3. POSTORDER
# ============================================================

# Rule:
# Left -> Right -> Root

# Shortcut:
# L R R
# (Left, Right, Root)

# Code:

def postorder(root):

    if root is None:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.val, end=" ")


# Example:
#
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
#
# Output:
#
# 4 5 2 6 7 3 1
#
# Memory Trick:
# Parent Last


# ============================================================
# GOLDEN RULE
# ============================================================

# Preorder
#
# print()
# Left
# Right

# Inorder
#
# Left
# print()
# Right

# Postorder
#
# Left
# Right
# print()


# ============================================================
# INTERVIEW TRICK
# ============================================================

# Sirf print() ki position badalne se traversal badal jata hai.

# print pehle     -> Preorder
# print beech me  -> Inorder
# print last      -> Postorder


# ============================================================
# TIME COMPLEXITY
# ============================================================

# Preorder   : O(n)
# Inorder    : O(n)
# Postorder  : O(n)


# ============================================================
# SPACE COMPLEXITY
# ============================================================

# O(h)

# h = Height of Tree


# ============================================================
# ONE LINE REVISION
# ============================================================

# Preorder  = Root Left Right
# Inorder   = Left Root Right
# Postorder = Left Right Root
#
# Bas print() ki position yaad rakho.
# ============================================================