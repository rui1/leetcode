class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        while root is not None:
            across = root
            while across is not None:
                if across.right is not None and across.left is not None:
                    across.left.next = across.right
                if across.right is not None and across.next is not None:
                    across.right.next =across.next.left
                across = across.next
            root= root.left
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return 
        else:
            across = root
            while across is not None:
                if across.right is not None and across.left is not None:
                    across.left.next =across.right
                if across.right is not None and across.next is not None:
                    across.right.next = across.next.left
                across = across.next
            return self.connect(root.left)
