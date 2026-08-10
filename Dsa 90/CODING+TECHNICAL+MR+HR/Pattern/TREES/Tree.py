# class TreeNode:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None

#     def preorder(root):
#         if root in None:
#             return 
#         print(root.val, end='')
#     preorder()
            

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(7)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(2)
# root.right.left = TreeNode(1)


# ============================================================
# Tree Node
# ============================================================

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ============================================================
# Preorder Traversal
# ============================================================

def preorder(root):

    if root is None:
        return

    print(root.val, end=" ")

    preorder(root.left)

    preorder(root.right)


# ============================================================
# Creating Tree
# ============================================================

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(20)

root.left.left = TreeNode(3)
root.left.right = TreeNode(8)

root.right.right = TreeNode(30)


# ============================================================
# Function Call
# ============================================================

preorder(root)

print('\n')


class postorder:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    # postorder  L N R

def postordered(root):
    if root is None:
        return
    postordered(root.left)
    print(root.val,end=' ')
    postordered(root.right)

root = postorder(10)

root.left = postorder(20)
root.right = postorder(30)

root.left.left = postorder(10)
root.left.right = postorder(15)

root.right.right = postorder(20)
root.right.left = postorder(10)



postordered(root)


print('\n')


class postorder:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    # postorder  L  R N

def postordered(root):
    if root is None:
        return
    postordered(root.left)
    postordered(root.right)
    print(root.val,end=' ')

root = postorder(10)

root.left = postorder(20)
root.right = postorder(30)

root.left.left = postorder(10)
root.left.right = postorder(15)

root.right.right = postorder(20)
root.right.left = postorder(10)



postordered(root)