from collections import deque

# -----------------------------
# Tree Node Class
# -----------------------------
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -----------------------------
# BFS (Level Order Traversal)
# -----------------------------
def level_order(root):

    if root is None:
        return

    queue = deque()

    queue.append(root)

    while queue:

        current = queue.popleft()

        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# -----------------------------
# Create Binary Tree
# -----------------------------
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


# -----------------------------
# Call Function
# -----------------------------
print("Level Order Traversal:")

level_order(root)