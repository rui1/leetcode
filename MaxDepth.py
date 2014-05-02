def maxDepth(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    elif root.left is not None and root.right is None:
        return 1+maxDept(root.left)
    elif root.right is not None and root.left is None:
        return 1+maxDepth(root.right)
    else:
        return 1+ max(maxDept(root.right),maxDept(root.left))
def maxDepth1(root):
    if root is None:
        return 0
    else:
        return 1+max(maxDept(root.right),maxDept(root.left))
